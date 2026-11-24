from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetEffectiveHoursOfOperationsRequest(BaseModel):
    InstanceId: StrictStr
    HoursOfOperationId: StrictStr
    FromDate: StrictStr
    ToDate: StrictStr
