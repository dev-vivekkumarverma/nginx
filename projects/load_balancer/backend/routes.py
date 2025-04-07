from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import socket

router = APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    client_ip = request.client.host
    client_port = request.client.port

    # Get IP of the original client if passed through a proxy (NGINX)
    forwarded_ip = request.headers.get("X-Forwarded-For", "Not Available")

    # Get the server (FastAPI backend) local IP
    try:
        server_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        server_ip = "Unavailable"

    return templates.TemplateResponse("index.html", context={
        "client_ip": client_ip,
        "client_port": client_port,
        "forwarded_ip": forwarded_ip,
        "server_ip": server_ip,
        "client_name": "Vivek Kumar Verma",
        "request": request
    })
