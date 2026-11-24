from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisassociateHoursOfOperationsRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    ParentHoursOfOperationIds: list[StrictStr]
