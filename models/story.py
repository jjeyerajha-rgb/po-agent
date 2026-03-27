from pydantic import BaseModel, Field


class AcceptanceCriterion(BaseModel):
    scenario: str = ""
    given: str = ""
    when: str = ""
    then: str = ""


class UserStory(BaseModel):
    title: str = ""
    persona: str = ""
    goal: str = ""
    benefit: str = ""
    acceptance_criteria: list[AcceptanceCriterion] = Field(default_factory=list)
    story_points: int | None = None
    labels: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    notes: str = ""

    @property
    def formatted(self) -> str:
        return (
            f"**As a** {self.persona}, "
            f"**I want** {self.goal}, "
            f"**so that** {self.benefit}"
        )
