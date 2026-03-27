from datetime import date
from pydantic import BaseModel, Field


class Sprint(BaseModel):
    name: str = ""
    goal: str = ""
    start_date: date | None = None
    end_date: date | None = None
    capacity: int = 0
    velocity: int = 0
    items: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
