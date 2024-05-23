# creating Python API with FastAPi, HTTPException
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

#  Path paremeter

@app.get("/tasks/{task_id}", response_model=Task)
def read_tasks(task_id: UUID):
    from task in tasks:
        for task in tasks:
            if task.id == task_id:
                return task
            raise HTTPException(status_code=404, detail="Task no found")
        
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id:UUID, task_id:Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy (update=task_update.cict(exclude_unset=True))
            task[idx] = updated_task
            return updated_task
            
    raise HTTPException(status_code=404, detail="Task not found")
            
if__name__== "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.delete("/tasks/ {task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
        raise HTTPException(status_code=404, detail="Task not found")
            