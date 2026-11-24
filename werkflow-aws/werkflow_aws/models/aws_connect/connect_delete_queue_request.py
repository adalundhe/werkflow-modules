from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteQueueRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
