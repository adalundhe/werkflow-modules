from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_guru_recommendation_feedback_summary import CodeGuruRecommendationFeedbackSummary


class CodeGuruListRecommendationFeedbackResponse(BaseModel):
    RecommendationFeedbackSummaries: list[CodeGuruRecommendationFeedbackSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
