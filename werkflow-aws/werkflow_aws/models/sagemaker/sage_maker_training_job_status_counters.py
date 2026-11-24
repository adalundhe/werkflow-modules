from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerTrainingJobStatusCounters(BaseModel):
    Completed: StrictInt | None = None
    InProgress: StrictInt | None = None
    RetryableError: StrictInt | None = None
    NonRetryableError: StrictInt | None = None
    Stopped: StrictInt | None = None
