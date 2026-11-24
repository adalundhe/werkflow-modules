from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GlueWorkflowRunStatistics(BaseModel):
    TotalActions: StrictInt | None = None
    TimeoutActions: StrictInt | None = None
    FailedActions: StrictInt | None = None
    StoppedActions: StrictInt | None = None
    SucceededActions: StrictInt | None = None
    RunningActions: StrictInt | None = None
    ErroredActions: StrictInt | None = None
    WaitingActions: StrictInt | None = None
