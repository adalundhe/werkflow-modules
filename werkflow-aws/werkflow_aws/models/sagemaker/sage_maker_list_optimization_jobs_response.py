from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_optimization_job_summary import SageMakerOptimizationJobSummary


class SageMakerListOptimizationJobsResponse(BaseModel):
    OptimizationJobSummaries: list[SageMakerOptimizationJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
