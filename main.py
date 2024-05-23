# creating Python API with FastAPi

from fastapi import FastAPI

from pydantic import BaseModel
from typing import list, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Task(BaseModel):
    id:Optional[UUID] = None
    title: str
    description:Optional[str] = None
    completed: bool = True

task = []

@pp.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task

# basic root 
@app.get("/tasks/", response_model=list[Task])
def read_tasks():
    return { "hello": "world!"}


if__name__== "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
