from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSGetQueueUrlResponse(BaseModel):
    QueueUrl: StrictStr | None = None
