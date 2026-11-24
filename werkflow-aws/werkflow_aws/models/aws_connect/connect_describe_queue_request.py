from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeQueueRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
