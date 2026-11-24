from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_solution import PersonalizeSolution


class PersonalizeDescribeSolutionResponse(BaseModel):
    solution: PersonalizeSolution | None = None
    ResponseMetadata: dict[str, Any] | None = None
