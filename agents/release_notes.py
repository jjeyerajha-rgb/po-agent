from agents.base_agent import BaseAgent
from utils.prompts import RELEASE_NOTES_SYSTEM, RELEASE_NOTES_USER


class ReleaseNotesAgent(BaseAgent):
    name = "Release Notes Generator"
    description = "Generate professional release notes and changelogs for any audience"
    icon = "📦"

    def get_system_prompt(self) -> str:
        return RELEASE_NOTES_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return RELEASE_NOTES_USER.format(
            version=kwargs.get("version", ""),
            release_date=kwargs.get("release_date", "TBD"),
            audience=kwargs.get("audience", "End users"),
            items=kwargs.get("items", ""),
            known_issues=kwargs.get("known_issues", "None"),
            context=kwargs.get("context", ""),
        )
