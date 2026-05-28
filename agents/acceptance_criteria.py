from agents.base_agent import BaseAgent
from utils.prompts import ACCEPTANCE_CRITERIA_SYSTEM, ACCEPTANCE_CRITERIA_USER


class AcceptanceCriteriaAgent(BaseAgent):
    name = "Acceptance Criteria Generator"
    description = "Generate comprehensive Given/When/Then acceptance criteria covering happy paths, edge cases, and errors"
    icon = "✅"

    def get_system_prompt(self) -> str:
        return ACCEPTANCE_CRITERIA_SYSTEM

    def build_user_prompt(self, **kwargs: str) -> str:
        return ACCEPTANCE_CRITERIA_USER.format(
            story=kwargs.get("story", ""),
            context=kwargs.get("context", "Not specified"),
            nfr=kwargs.get("nfr", "Standard performance and accessibility"),
            edge_cases=kwargs.get("edge_cases", "Consider common edge cases"),
        )
