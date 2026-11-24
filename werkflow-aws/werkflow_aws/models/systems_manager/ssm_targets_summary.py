from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SSMTargetsSummary(BaseModel):
    TotalCount: StrictInt | None = None
    StartedCount: StrictInt | None = None
    CompletedCount: StrictInt | None = None
    SuccessfulCount: StrictInt | None = None
    FailedCount: StrictInt | None = None
