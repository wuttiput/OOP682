from fastapi import FastAPI, Depends
from typing import List
from .model import Task, TaskCreate
from .repositories import InMemoryTaskRepository, ITaskRepository, SqlTaskRepository
from .services import TaskService
from .database import SessionLocal
from sqlalchemy.orm import Session
from .database import engine
from . import model_orm

model_orm.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Singleton Repository Instance
# task_repo = InMemoryTaskRepository()

def get_db():
    db = SessionLocal()  # เปิดประตูบ้านของจริงแล้ว
    try:
        yield db
    finally:
        db.close()


# Dependency Provider
# def get_task_service():
#     return TaskService(task_repo)
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate,
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)

@app.put("/tasks/{task_id}/complete", response_model=Task)
def complete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    return service.mark_task_completed(task_id)