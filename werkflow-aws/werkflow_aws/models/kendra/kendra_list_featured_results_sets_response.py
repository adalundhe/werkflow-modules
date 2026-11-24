from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_featured_results_set_summary import KendraFeaturedResultsSetSummary


class KendraListFeaturedResultsSetsResponse(BaseModel):
    FeaturedResultsSetSummaryItems: list[KendraFeaturedResultsSetSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
