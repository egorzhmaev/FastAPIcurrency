from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login/", response_class=HTMLResponse)
async def login_for_access_token(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("login.html", context)

@router.get("/registration/", response_class=HTMLResponse)
async def login_for_access_token(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("registration.html", context)