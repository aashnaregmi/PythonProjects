from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TodoCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "Todo API running"}
