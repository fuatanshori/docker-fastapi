from typing import Union

from fastapi import FastAPI
app = FastAPI()

@app.get("/{name}")
def helloName(name):
    return {"message": f"hello {name}"}