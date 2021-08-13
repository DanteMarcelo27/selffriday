from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def raiz():
    return {"rock in roll"}