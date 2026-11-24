from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_experiences_summary import KendraExperiencesSummary


class KendraListExperiencesResponse(BaseModel):
    SummaryItems: list[KendraExperiencesSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
