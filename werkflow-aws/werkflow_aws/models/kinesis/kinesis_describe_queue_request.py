from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisDescribeQueueRequest(BaseModel):
    QueueARN: StrictStr
