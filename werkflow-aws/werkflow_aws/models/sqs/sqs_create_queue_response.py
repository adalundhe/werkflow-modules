from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSCreateQueueResponse(BaseModel):
    QueueUrl: StrictStr | None = None
