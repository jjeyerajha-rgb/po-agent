from abc import ABC, abstractmethod

from utils.llm_client import chat


class BaseAgent(ABC):
    """Base class for all PO Agent capabilities."""

    name: str = "Base Agent"
    description: str = ""
    icon: str = "🤖"

    @abstractmethod
    def get_system_prompt(self) -> str: ...

    @abstractmethod
    def build_user_prompt(self, **kwargs: str) -> str: ...

    def run(self, **kwargs: str) -> str:
        system_prompt = self.get_system_prompt()
        user_prompt = self.build_user_prompt(**kwargs)
        return chat(system_prompt, user_prompt)
