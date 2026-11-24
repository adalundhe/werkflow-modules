from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_search_sample_queries_search_result import CloudTrailSearchSampleQueriesSearchResult


class CloudTrailSearchSampleQueriesResponse(BaseModel):
    SearchResults: list[CloudTrailSearchSampleQueriesSearchResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
