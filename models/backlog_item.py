from enum import Enum
from pydantic import BaseModel, Field


class Priority(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class ItemType(str, Enum):
    FEATURE = "Feature"
    BUG = "Bug"
    TECH_DEBT = "Tech Debt"
    SPIKE = "Spike"
    CHORE = "Chore"


class BacklogItem(BaseModel):
    id: str = ""
    title: str = ""
    description: str = ""
    item_type: ItemType = ItemType.FEATURE
    priority: Priority = Priority.MEDIUM
    story_points: int | None = None
    labels: list[str] = Field(default_factory=list)
    status: str = "New"
