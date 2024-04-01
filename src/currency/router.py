from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from auth.base_config import current_user
from currency.external_api import currency_list, currency_convert
from currency.schemas import CurrencyPair

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/', response_class=HTMLResponse, dependencies=[Depends(current_user)])
def root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@router.get('/list/', response_class=HTMLResponse, dependencies=[Depends(current_user)])
def root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("list.html", context)

@router.get('/get_list/', dependencies=[Depends(current_user)])
async def get_currency_list():
    data = currency_list()
    return data

@router.get('/exchange/', dependencies=[Depends(current_user)])
async def get_currency_exchange(pair: CurrencyPair = Depends()):
    data = currency_convert(pair)
    return data
