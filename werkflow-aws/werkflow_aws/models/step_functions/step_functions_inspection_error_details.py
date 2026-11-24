from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StepFunctionsInspectionErrorDetails(BaseModel):
    catchIndex: StrictInt | None = None
    retryIndex: StrictInt | None = None
    retryBackoffIntervalSeconds: StrictInt | None = None
