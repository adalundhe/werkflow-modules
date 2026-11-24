from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WorkSpacesCapacity(BaseModel):
    DesiredUserSessions: StrictInt
