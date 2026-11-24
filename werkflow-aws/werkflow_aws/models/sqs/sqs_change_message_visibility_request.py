from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SQSChangeMessageVisibilityRequest(BaseModel):
    QueueUrl: StrictStr
    ReceiptHandle: StrictStr
    VisibilityTimeout: StrictInt
