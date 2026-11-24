from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_recommendation_job_summary import SageMakerAIRecommendationJobSummary


class SageMakerListAIRecommendationJobsResponse(BaseModel):
    AIRecommendationJobs: list[SageMakerAIRecommendationJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
