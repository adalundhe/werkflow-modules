from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteHoursOfOperationOverrideRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    HoursOfOperationOverrideId: StrictStr
