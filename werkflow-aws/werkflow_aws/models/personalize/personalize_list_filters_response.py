from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .personalize_filter_summary import PersonalizeFilterSummary


class PersonalizeListFiltersResponse(BaseModel):
    Filters: list[PersonalizeFilterSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
