from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_guru_recommendation_summary import CodeGuruRecommendationSummary


class CodeGuruListRecommendationsResponse(BaseModel):
    RecommendationSummaries: list[CodeGuruRecommendationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
