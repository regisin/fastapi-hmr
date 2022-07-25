from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils import reloader

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title='Potato',
    openapi_url=None,
    docs_url=None,
    redoc_url=None,
)



@app.get("/", status_code=200, response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('Home.html', {"request": request,
                                                "reloader": reloader,
                                                "title":"Totato"})



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        data = await websocket.receive_text()
    except WebSocketDisconnect:
        pass
