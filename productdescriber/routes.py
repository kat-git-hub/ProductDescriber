from pathlib import Path
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .generator import generate_description

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse(request, "index.html")


@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, product: str = Form(...), style: str = Form(...)):
    try:
        result = await generate_description(product, style)
    except Exception as e:
        result = f"Error: {e}"
    return templates.TemplateResponse(request, "index.html", {"result": result})
