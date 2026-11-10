"""Golden dataset record schema: user story in, expert-written reference test cases out."""

from enum import Enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

Text = Annotated[str, StringConstraints(strip_whitespace=True, min_length=5)]


class Difficulty(str, Enum):
    EASY = "easy"
    AMBIGUOUS = "ambiguous"  # vague or conflicting acceptance criteria
    EDGE = "edge"  # boundaries, negative paths, unusual states


class ReferenceTestCase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=5)
    preconditions: Text
    steps: list[Text] = Field(min_length=1)
    expected: str = Field(min_length=5)


class GoldenRecord(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=r"^us-\d{3}$")
    domain: str = Field(min_length=2)
    story: str = Field(min_length=20)
    acceptance_criteria: list[Text] = Field(min_length=1)
    reference_test_cases: list[ReferenceTestCase] = Field(min_length=2)
    difficulty: Difficulty
    notes: str = ""  # why this case is hard, what an LLM is likely to miss
