from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSDeleteMessageRequest(BaseModel):
    QueueUrl: StrictStr
    ReceiptHandle: StrictStr
