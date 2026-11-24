from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_guru_recommendation_feedback import CodeGuruRecommendationFeedback


class CodeGuruDescribeRecommendationFeedbackResponse(BaseModel):
    RecommendationFeedback: CodeGuruRecommendationFeedback | None = None
    ResponseMetadata: dict[str, Any] | None = None
