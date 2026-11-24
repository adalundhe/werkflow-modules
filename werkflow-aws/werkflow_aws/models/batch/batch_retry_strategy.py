from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_evaluate_on_exit import BatchEvaluateOnExit


class BatchRetryStrategy(BaseModel):
    attempts: StrictInt | None = None
    evaluateOnExit: list[BatchEvaluateOnExit] | None = None
