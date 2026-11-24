from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSDeleteMessageBatchRequestEntry(BaseModel):
    Id: StrictStr
    ReceiptHandle: StrictStr
