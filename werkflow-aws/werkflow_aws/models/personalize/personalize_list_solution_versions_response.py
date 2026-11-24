from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_solution_version_summary import PersonalizeSolutionVersionSummary


class PersonalizeListSolutionVersionsResponse(BaseModel):
    solutionVersions: list[PersonalizeSolutionVersionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
