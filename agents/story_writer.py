from agents.base_agent import BaseAgent
from utils.prompts import STORY_WRITER_SYSTEM, STORY_WRITER_USER


class StoryWriterAgent(BaseAgent):
    name = "User Story Writer"
    description = "Generate well-structured user stories with acceptance criteria following INVEST principles"
    icon = "📝"

    def get_system_prompt(self) -> str:
        return STORY_WRITER_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return STORY_WRITER_USER.format(
            context=kwargs.get("context", "Not specified"),
            requirements=kwargs.get("requirements", ""),
            personas=kwargs.get("personas", "End user"),
            notes=kwargs.get("notes", "None"),
        )
