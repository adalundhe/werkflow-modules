from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_batch_stop_job_run_error import GlueBatchStopJobRunError
from .glue_batch_stop_job_run_successful_submission import GlueBatchStopJobRunSuccessfulSubmission


class GlueBatchStopJobRunResponse(BaseModel):
    SuccessfulSubmissions: list[GlueBatchStopJobRunSuccessfulSubmission] | None = None
    Errors: list[GlueBatchStopJobRunError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
