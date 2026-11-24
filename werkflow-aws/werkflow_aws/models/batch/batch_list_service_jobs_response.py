from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_service_job_summary import BatchServiceJobSummary


class BatchListServiceJobsResponse(BaseModel):
    jobSummaryList: list[BatchServiceJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
