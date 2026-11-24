from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WorkSpacesCapacityStatus(BaseModel):
    AvailableUserSessions: StrictInt | None = None
    DesiredUserSessions: StrictInt | None = None
    ActualUserSessions: StrictInt | None = None
    ActiveUserSessions: StrictInt | None = None
