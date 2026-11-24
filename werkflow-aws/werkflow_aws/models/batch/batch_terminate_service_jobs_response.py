from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_terminate_service_jobs_error_detail import BatchTerminateServiceJobsErrorDetail


class BatchTerminateServiceJobsResponse(BaseModel):
    successful: list[StrictStr] | None = None
    errors: list[BatchTerminateServiceJobsErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
