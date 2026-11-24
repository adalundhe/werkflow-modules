from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateQueueStatusRequest(BaseModel):
    InstanceId: StrictStr
    QueueId: StrictStr
    Status: Literal['ENABLED', 'DISABLED']
