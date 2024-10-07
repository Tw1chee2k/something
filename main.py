from typing import Annotated, Optional
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class StaskAdd(BaseModel):
    name: str
    description: Optional[str] | None

class STask(BaseModel):
    id: int


# @app.get("/tasks")
# def get_tasks():
#     task = STask(name = "Запиши это видео")
#     return {"data": task}

@app.post("/tasks")
async def add_task(
    task: Annotated[StaskAdd, Depends()],
):
    tasks.append(tasks)
    return {"ok": True}

