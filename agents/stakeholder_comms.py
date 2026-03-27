from agents.base_agent import BaseAgent
from utils.prompts import STAKEHOLDER_COMMS_SYSTEM, STAKEHOLDER_COMMS_USER


class StakeholderCommsAgent(BaseAgent):
    name = "Stakeholder Communications"
    description = "Draft status updates, executive summaries, and stakeholder-tailored communications"
    icon = "💬"

    def get_system_prompt(self) -> str:
        return STAKEHOLDER_COMMS_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return STAKEHOLDER_COMMS_USER.format(
            comm_type=kwargs.get("comm_type", "Status Update"),
            audience=kwargs.get("audience", ""),
            message=kwargs.get("message", ""),
            context=kwargs.get("context", ""),
            data=kwargs.get("data", "None provided"),
            tone=kwargs.get("tone", "Professional"),
        )
