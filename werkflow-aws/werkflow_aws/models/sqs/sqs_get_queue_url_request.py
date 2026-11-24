from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSGetQueueUrlRequest(BaseModel):
    QueueName: StrictStr
    QueueOwnerAWSAccountId: StrictStr | None = None
