from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectRoutingProfileQueueReference(BaseModel):
    QueueId: StrictStr
    Channel: Literal['VOICE', 'CHAT', 'TASK', 'EMAIL']
