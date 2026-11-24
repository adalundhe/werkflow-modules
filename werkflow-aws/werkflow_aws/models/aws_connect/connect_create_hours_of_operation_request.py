from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_hours_of_operation_config import ConnectHoursOfOperationConfig
from .connect_parent_hours_of_operation_config import ConnectParentHoursOfOperationConfig


class ConnectCreateHoursOfOperationRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    TimeZone: StrictStr
    Config: list[ConnectHoursOfOperationConfig]
    Description: StrictStr | None = None
    ParentHoursOfOperationConfigs: list[ConnectParentHoursOfOperationConfig] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
