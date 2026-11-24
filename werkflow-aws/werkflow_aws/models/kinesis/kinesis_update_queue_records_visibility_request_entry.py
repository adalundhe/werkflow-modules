from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisUpdateQueueRecordsVisibilityRequestEntry(BaseModel):
    ReceiptHandle: StrictStr
    VisibilityTimeoutSeconds: StrictInt
