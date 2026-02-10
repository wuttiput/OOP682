from .repositories import ITaskRepository,SqlTaskRepository
from .model import TaskCreate
from fastapi import HTTPException, status

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Validation: Check if title already exists
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Task with title '{task_in.title}' already exists"
            )
        return self.repo.create(task_in)
    
    def mark_task_completed(self, task_id: int):
        return self.repo.update_task_completed(task_id, True)