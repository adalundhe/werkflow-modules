from __future__ import annotations
from pydantic import BaseModel, StrictInt


class StepFunctionsMapRunExecutionCounts(BaseModel):
    pending: StrictInt | None = None
    running: StrictInt | None = None
    succeeded: StrictInt | None = None
    failed: StrictInt | None = None
    timedOut: StrictInt | None = None
    aborted: StrictInt | None = None
    total: StrictInt | None = None
    resultsWritten: StrictInt | None = None
    failuresNotRedrivable: StrictInt | None = None
    pendingRedrive: StrictInt | None = None
