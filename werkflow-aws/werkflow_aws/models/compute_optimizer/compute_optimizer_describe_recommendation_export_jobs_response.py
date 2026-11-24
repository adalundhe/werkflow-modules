from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_recommendation_export_job import ComputeOptimizerRecommendationExportJob


class ComputeOptimizerDescribeRecommendationExportJobsResponse(BaseModel):
    recommendationExportJobs: list[ComputeOptimizerRecommendationExportJob] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
