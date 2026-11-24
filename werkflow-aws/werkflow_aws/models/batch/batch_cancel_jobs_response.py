from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_cancel_jobs_error_detail import BatchCancelJobsErrorDetail


class BatchCancelJobsResponse(BaseModel):
    successful: list[StrictStr] | None = None
    errors: list[BatchCancelJobsErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
