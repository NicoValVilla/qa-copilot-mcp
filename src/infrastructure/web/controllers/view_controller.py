from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/infrastructure/web/templates")
router = APIRouter(tags=["Web"])


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
