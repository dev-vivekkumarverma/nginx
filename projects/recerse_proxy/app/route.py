from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router=APIRouter()


teplates=Jinja2Templates(directory='template')

@router.get("/", response_class=HTMLResponse)
async def home(request:Request):
    client_ip= request.client.host
    client_port= request.client.port

    return teplates.TemplateResponse('index.html', context={
        "client_ip":client_ip,
        "client_port":client_port,
        "client_name":"Vivek Kumar Verma",
        "request":request,
    })