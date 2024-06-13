"""
    schemas.py
"""
from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    name: str
    description: Optional[str] = None # Может быть пустым str | None


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int
