from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_solution_version import PersonalizeSolutionVersion


class PersonalizeDescribeSolutionVersionResponse(BaseModel):
    solutionVersion: PersonalizeSolutionVersion | None = None
    ResponseMetadata: dict[str, Any] | None = None
