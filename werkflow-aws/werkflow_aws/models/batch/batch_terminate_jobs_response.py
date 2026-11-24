from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_terminate_jobs_error_detail import BatchTerminateJobsErrorDetail


class BatchTerminateJobsResponse(BaseModel):
    successful: list[StrictStr] | None = None
    errors: list[BatchTerminateJobsErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
