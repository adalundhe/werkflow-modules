from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_override_time_slice import ConnectOverrideTimeSlice


class ConnectHoursOfOperationOverrideConfig(BaseModel):
    Day: StrictStr | None = None
    StartTime: ConnectOverrideTimeSlice | None = None
    EndTime: ConnectOverrideTimeSlice | None = None
