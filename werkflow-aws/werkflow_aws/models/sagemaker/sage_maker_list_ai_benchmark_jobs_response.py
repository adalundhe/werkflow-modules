from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_benchmark_job_summary import SageMakerAIBenchmarkJobSummary


class SageMakerListAIBenchmarkJobsResponse(BaseModel):
    AIBenchmarkJobs: list[SageMakerAIBenchmarkJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
