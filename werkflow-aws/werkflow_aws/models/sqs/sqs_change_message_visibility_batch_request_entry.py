from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SQSChangeMessageVisibilityBatchRequestEntry(BaseModel):
    Id: StrictStr
    ReceiptHandle: StrictStr
    VisibilityTimeout: StrictInt | None = None
