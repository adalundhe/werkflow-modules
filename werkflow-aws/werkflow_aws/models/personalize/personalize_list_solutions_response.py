from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_solution_summary import PersonalizeSolutionSummary


class PersonalizeListSolutionsResponse(BaseModel):
    solutions: list[PersonalizeSolutionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
