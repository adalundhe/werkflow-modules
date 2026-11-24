from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_service_job_evaluate_on_exit import BatchServiceJobEvaluateOnExit


class BatchServiceJobRetryStrategy(BaseModel):
    attempts: StrictInt | None = None
    evaluateOnExit: list[BatchServiceJobEvaluateOnExit] | None = None
