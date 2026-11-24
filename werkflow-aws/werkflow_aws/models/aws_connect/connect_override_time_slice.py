from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ConnectOverrideTimeSlice(BaseModel):
    Hours: StrictInt | None = None
    Minutes: StrictInt | None = None
