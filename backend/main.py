import os
import uuid
import json
import base64
import re
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Initialize Hugging Face Client
# It automatically picks up HUGGINGFACE_API_KEY from your .env
client = InferenceClient(api_key=os.environ.get("HUGGINGFACE_API_KEY"))

generated_sites = {}

class GenerationRequest(BaseModel):
    prompt: str

def extract_json(text: str) -> str:
    """Robustly extracts JSON from open-source model outputs."""
    # Uses regular expressions to find the first '{' and the last '}'
    match = re.search(r'\{[\s\S]*\}', text)
    if match:
        return match.group(0)
    return text

@app.post("/api/generate")
async def generate_site(request: GenerationRequest):
    system_prompt = """
    You are an expert full-stack web developer. 
    The user will describe a website. You must generate the HTML/CSS/JS AND write a highly detailed image generation prompt for the main hero/background image of the site.
    
    In your HTML, wherever the main image should go, use the exact string: IMAGE_PLACEHOLDER as the src.
    Example: <img src="IMAGE_PLACEHOLDER" alt="Hero Image">
    
    OUTPUT FORMAT:
    You must respond ONLY with a valid JSON object containing exactly two keys: "html" and "image_prompt".
    Do not include markdown tags. Do not write anything outside the JSON object.
    """
    
    try:
        # Step 1: Text & Code Gen (Using Qwen 2.5 Coder - excellent for web dev)
        text_response = client.chat_completion(
            model="Qwen/Qwen2.5-Coder-32B-Instruct",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.prompt}
            ],
            max_tokens=4000
        )
        
        # Clean and parse the output using our robust extractor
        raw_text = text_response.choices[0].message.content
        clean_json_str = extract_json(raw_text)
        data = json.loads(clean_json_str)
        
        site_html = data.get("html", "<h1>Error generating HTML</h1>")
        image_prompt = data.get("image_prompt", "A beautiful abstract background")
        
        # Step 2: Image Gen (Using Stable Diffusion XL)
        # text_to_image automatically returns a Pillow (PIL) Image object
        img = client.text_to_image(
            prompt=image_prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0"
        )
        
        # Convert the Pillow image to a base64 string
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        img_data_url = f"data:image/png;base64,{img_str}"
        
        # Step 3: Inject the image into the HTML
        final_html = site_html.replace("IMAGE_PLACEHOLDER", img_data_url)
        
        # Save and return the unified site
        site_id = str(uuid.uuid4())
        generated_sites[site_id] = final_html
        
        return {
            "success": True,
            "site_id": site_id,
            "html": final_html,
            "url": f"/site/{site_id}"
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/site/{site_id}", response_class=HTMLResponse)
async def serve_generated_site(site_id: str):
    if site_id in generated_sites:
        return generated_sites[site_id]
    return HTMLResponse("<h1>404 - Site Not Found</h1>", status_code=404)

@app.get("/", response_class=FileResponse)
async def read_index():
    # Automatically finds index.html in the main parent folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    return os.path.join(root_dir, "index.html")
