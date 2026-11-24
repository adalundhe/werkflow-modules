from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_job_summary import SageMakerJobSummary


class SageMakerListJobsResponse(BaseModel):
    NextToken: StrictStr | None = None
    JobSummaries: list[SageMakerJobSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
