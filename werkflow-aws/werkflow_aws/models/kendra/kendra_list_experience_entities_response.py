from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_experience_entities_summary import KendraExperienceEntitiesSummary


class KendraListExperienceEntitiesResponse(BaseModel):
    SummaryItems: list[KendraExperienceEntitiesSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
