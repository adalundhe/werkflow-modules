from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteHoursOfOperationRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
