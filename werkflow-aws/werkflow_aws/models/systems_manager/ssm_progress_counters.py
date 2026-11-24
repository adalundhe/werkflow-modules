from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SSMProgressCounters(BaseModel):
    TotalSteps: StrictInt | None = None
    SuccessSteps: StrictInt | None = None
    FailedSteps: StrictInt | None = None
    CancelledSteps: StrictInt | None = None
    TimedOutSteps: StrictInt | None = None
