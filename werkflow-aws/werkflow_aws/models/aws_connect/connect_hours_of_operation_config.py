from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_time_slice import ConnectHoursOfOperationTimeSlice


class ConnectHoursOfOperationConfig(BaseModel):
    Day: StrictStr | None = None
    StartTime: ConnectHoursOfOperationTimeSlice | None = None
    EndTime: ConnectHoursOfOperationTimeSlice | None = None
