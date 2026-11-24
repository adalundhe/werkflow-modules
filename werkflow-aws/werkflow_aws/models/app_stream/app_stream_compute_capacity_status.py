from __future__ import annotations
from pydantic import BaseModel, StrictInt


class AppStreamComputeCapacityStatus(BaseModel):
    Desired: StrictInt | None = None
    Running: StrictInt | None = None
    InUse: StrictInt | None = None
    Available: StrictInt | None = None
    DesiredUserSessions: StrictInt | None = None
    AvailableUserSessions: StrictInt | None = None
    ActiveUserSessions: StrictInt | None = None
    ActualUserSessions: StrictInt | None = None
    Draining: StrictInt | None = None
    DrainModeActiveUserSessions: StrictInt | None = None
    DrainModeUnusedUserSessions: StrictInt | None = None
