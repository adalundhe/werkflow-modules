from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_job_filter import ComputeOptimizerJobFilter


class ComputeOptimizerDescribeRecommendationExportJobsRequest(BaseModel):
    jobIds: list[StrictStr] | None = None
    filters: list[ComputeOptimizerJobFilter] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
