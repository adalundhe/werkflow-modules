from __future__ import annotations
from pydantic import BaseModel
from .connect_override_time_slice import ConnectOverrideTimeSlice


class ConnectOperationalHour(BaseModel):
    Start: ConnectOverrideTimeSlice | None = None
    End: ConnectOverrideTimeSlice | None = None
