from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_override_time_slice import ConnectOverrideTimeSlice


class ConnectOverrideHour(BaseModel):
    Start: ConnectOverrideTimeSlice | None = None
    End: ConnectOverrideTimeSlice | None = None
    OverrideName: StrictStr | None = None
    OperationalStatus: StrictStr | None = None
