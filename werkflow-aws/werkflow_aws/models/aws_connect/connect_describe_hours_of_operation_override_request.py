from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeHoursOfOperationOverrideRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    HoursOfOperationOverrideId: StrictStr
