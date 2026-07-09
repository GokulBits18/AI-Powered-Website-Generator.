#  AI Website Builder with AI Image Generation

An AI-powered website generation platform built with **FastAPI**, **Hugging Face Inference API**, **Qwen 2.5 Coder**, and **Stable Diffusion XL**. The application creates complete responsive websites from natural language prompts and automatically generates matching AI images to produce a visually appealing website.

---

#  Project Overview

AI Website Builder is a full-stack Generative AI application that transforms user descriptions into complete, responsive websites with automatically generated images.

The application uses **Qwen 2.5 Coder** to generate the HTML, CSS, and JavaScript for the website, while **Stable Diffusion XL** creates a custom AI-generated hero image based on the website's content. The generated image is embedded directly into the webpage, allowing users to preview and open the generated website instantly.

This project demonstrates how Large Language Models (LLMs) and AI image generation models can work together to automate modern web development.

---

#  Features

- Generate websites from text prompts
- AI-generated HTML, CSS, and JavaScript
- Automatic AI image generation
- Live website preview
- Open generated website in a new tab
- Responsive webpage generation
- JSON-based AI output parsing
- Base64 image embedding
- FastAPI REST API backend
- Simple HTML frontend
- Environment variable support
- Automatic unique website IDs

---

#  Technologies Used

- Python
- FastAPI
- Hugging Face Inference API
- Qwen 2.5 Coder
- Stable Diffusion XL
- HTML5
- CSS3
- JavaScript
- JSON
- REST API
- python-dotenv
- Artificial Intelligence
- Large Language Models (LLMs)

---

#  AI Models Used

### Text & Code Generation

**Qwen/Qwen2.5-Coder-32B-Instruct**

Generates:

- HTML
- CSS
- JavaScript
- AI image prompt

---

### Image Generation

**stabilityai/stable-diffusion-xl-base-1.0**

Generates:

- Hero images
- Website backgrounds
- Custom illustrations

---

#  How the System Works

The application follows these steps:

1. User enters a website description.
2. The prompt is sent to the FastAPI backend.
3. Qwen 2.5 Coder generates:
   - HTML
   - CSS
   - JavaScript
   - Image prompt
4. Stable Diffusion XL creates an AI-generated image.
5. The image is converted to Base64.
6. The image replaces the placeholder inside the generated HTML.
7. The completed website is rendered in a live preview.
8. Users can open the generated website in a separate browser tab.

---

#  Project Structure

```
AI-Website-Builder/
│
├── backend/
│   └── app.py
│
├── index.html
├── .env
├── requirements.txt
└── README.md
```

---

#  Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/ai-website-builder.git

cd ai-website-builder
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastapi uvicorn huggingface_hub python-dotenv pillow pydantic
```

---

#  Environment Variables

Create a `.env` file in the project folder.

```env
HUGGINGFACE_API_KEY=your_api_key
```

---

#  Running the Project

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

#  Code Workflow

### Step 1

User enters a website prompt.

Example:

```
Create a modern travel agency landing page with a beach hero section.
```

↓

### Step 2

Qwen 2.5 Coder generates structured JSON:

```json
{
  "html": "...",
  "image_prompt": "A tropical beach with luxury travel vibes..."
}
```

↓

### Step 3

Stable Diffusion XL creates the requested image.

↓

### Step 4

The image is converted into Base64 format.

↓

### Step 5

The placeholder inside the HTML is replaced with the generated image.

↓

### Step 6

The final website is displayed inside the live preview panel.

---

#  Example Output

### User Prompt

```
Create a portfolio website for a software developer with a futuristic dark theme.
```

Generated Output:

- Responsive landing page
- Animated UI
- AI-generated hero image
- Interactive JavaScript
- Live preview
- Standalone webpage

---

# Applications

- AI Website Builder
- Landing Page Generator
- Portfolio Generator
- Startup Website Creation
- Rapid Web Prototyping
- Educational AI Projects
- UI/UX Prototyping
- Marketing Website Generation
- AI-assisted Web Development

---

#  Future Improvements

- Multi-page website generation
- React and Next.js support
- Tailwind CSS generation
- Website ZIP download
- Editable code editor
- Authentication system
- Database storage
- Cloud deployment
- Custom AI image styles
- Website publishing feature

---

#  Learning Outcomes

This project demonstrates:

- FastAPI backend development
- REST API design
- Hugging Face Inference API integration
- Large Language Model (LLM) integration
- AI image generation
- Prompt engineering
- JSON parsing
- Base64 image processing
- HTML generation
- AI-powered web development

---


#  01000111 01101111 01101011 01110101 01101100

Developed using Python, FastAPI, Hugging Face Inference API, Qwen 2.5 Coder, and Stable Diffusion XL to demonstrate AI-powered website generation with automatic image creation and live preview capabilities.
