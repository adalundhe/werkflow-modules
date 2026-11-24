from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeHoursOfOperationRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
