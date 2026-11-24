from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisReceiveDeadLetterQueueRecordsRequest(BaseModel):
    QueueARN: StrictStr
    Limit: StrictInt | None = None
    WaitTimeSeconds: StrictInt | None = None
    VisibilityTimeoutSeconds: StrictInt | None = None
