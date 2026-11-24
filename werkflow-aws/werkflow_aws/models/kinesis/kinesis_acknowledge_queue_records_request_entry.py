from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAcknowledgeQueueRecordsRequestEntry(BaseModel):
    ReceiptHandle: StrictStr
