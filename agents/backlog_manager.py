from agents.base_agent import BaseAgent
from utils.prompts import BACKLOG_PRIORITIZE_SYSTEM, BACKLOG_PRIORITIZE_USER


class BacklogManagerAgent(BaseAgent):
    name = "Backlog Manager"
    description = "Prioritize and organize backlog items using proven frameworks (MoSCoW, WSJF, RICE)"
    icon = "📋"

    def get_system_prompt(self) -> str:
        return BACKLOG_PRIORITIZE_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return BACKLOG_PRIORITIZE_USER.format(
            items=kwargs.get("items", ""),
            framework=kwargs.get("framework", "RICE"),
            business_context=kwargs.get("business_context", "Not specified"),
            capacity=kwargs.get("capacity", "Not specified"),
        )
