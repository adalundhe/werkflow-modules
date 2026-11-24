from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_recommendation_error import AccessAnalyzerRecommendationError
from .access_analyzer_recommended_step import AccessAnalyzerRecommendedStep


class AccessAnalyzerGetFindingRecommendationResponse(BaseModel):
    startedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
    nextToken: StrictStr | None = None
    error: AccessAnalyzerRecommendationError | None = None
    resourceArn: StrictStr | None = None
    recommendedSteps: list[AccessAnalyzerRecommendedStep] | None = None
    recommendationType: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
