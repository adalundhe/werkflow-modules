from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_parent_hours_of_operation_config import ConnectParentHoursOfOperationConfig


class ConnectAssociateHoursOfOperationsRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    ParentHoursOfOperationConfigs: list[ConnectParentHoursOfOperationConfig]
