from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisUpdateDeadLetterQueueRecordsVisibilityRequestEntry(BaseModel):
    ReceiptHandle: StrictStr
    VisibilityTimeoutSeconds: StrictInt
