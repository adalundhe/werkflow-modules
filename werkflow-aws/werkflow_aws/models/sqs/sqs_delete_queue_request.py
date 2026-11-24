from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSDeleteQueueRequest(BaseModel):
    QueueUrl: StrictStr
