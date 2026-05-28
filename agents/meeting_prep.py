from agents.base_agent import BaseAgent
from utils.prompts import MEETING_PREP_SYSTEM, MEETING_PREP_USER


class MeetingPrepAgent(BaseAgent):
    name = "Meeting Prep Assistant"
    description = "Prepare agendas, talking points, and materials for sprint ceremonies and stakeholder meetings"
    icon = "📅"

    def get_system_prompt(self) -> str:
        return MEETING_PREP_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return MEETING_PREP_USER.format(
            meeting_type=kwargs.get("meeting_type", ""),
            attendees=kwargs.get("attendees", ""),
            duration=kwargs.get("duration", "60 minutes"),
            objectives=kwargs.get("objectives", ""),
            context=kwargs.get("context", ""),
            action_items=kwargs.get("action_items", "None"),
        )
