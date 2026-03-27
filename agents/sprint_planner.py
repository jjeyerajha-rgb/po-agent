from agents.base_agent import BaseAgent
from utils.prompts import SPRINT_PLANNER_SYSTEM, SPRINT_PLANNER_USER


class SprintPlannerAgent(BaseAgent):
    name = "Sprint Planner"
    description = "Plan sprints with goal setting, capacity planning, and balanced item selection"
    icon = "🏃"

    def get_system_prompt(self) -> str:
        return SPRINT_PLANNER_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return SPRINT_PLANNER_USER.format(
            duration=kwargs.get("duration", "2 weeks"),
            capacity=kwargs.get("capacity", "Not specified"),
            velocity=kwargs.get("velocity", "Not specified"),
            goals=kwargs.get("goals", ""),
            backlog_items=kwargs.get("backlog_items", ""),
            carryover=kwargs.get("carryover", "None"),
            risks=kwargs.get("risks", "None identified"),
        )
