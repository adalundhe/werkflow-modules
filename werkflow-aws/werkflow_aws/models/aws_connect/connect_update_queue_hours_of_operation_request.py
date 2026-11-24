from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdateQueueHoursOfOperationRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    HoursOfOperationId: StrictStr
