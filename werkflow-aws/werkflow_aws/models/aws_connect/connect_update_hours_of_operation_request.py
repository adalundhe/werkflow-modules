from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_config import ConnectHoursOfOperationConfig


class ConnectUpdateHoursOfOperationRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    TimeZone: StrictStr | None = None
    Config: list[ConnectHoursOfOperationConfig] | None = None
