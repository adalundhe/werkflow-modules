from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSUntagQueueRequest(BaseModel):
    QueueUrl: StrictStr
    TagKeys: list[StrictStr]
