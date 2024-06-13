"""
    router.py
"""
from typing import Annotated, List
from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask, STaskId
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Добавление
@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    """ Add a row """
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> List[STask]:
    """ Get all rows """
    tasks = await TaskRepository.find_all()
    return tasks
