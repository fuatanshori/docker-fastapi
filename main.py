from typing import Union

from fastapi import FastAPI,WebSocket
app = FastAPI()

@app.get("/")
def home():
    return {"message":"hello world"}

@app.get("/{name}")
def helloName(name):
    return {"message": f"hello {name}"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")