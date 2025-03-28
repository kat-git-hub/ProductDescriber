from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate_description(
    request: Request,
    product: str = Form(...),
    style: str = Form(...)
):
    prompt = f"Write a product description in {style} style. Here is the data: {product}"

    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=data)
        result = response.json().get("response", "No response from the model")
    except Exception as e:
        result = f"Error: {e}"

    return templates.TemplateResponse("index.html", {"request": request, "result": result})
