from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_job_summary import BatchJobSummary


class BatchListJobsResponse(BaseModel):
    jobSummaryList: list[BatchJobSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
