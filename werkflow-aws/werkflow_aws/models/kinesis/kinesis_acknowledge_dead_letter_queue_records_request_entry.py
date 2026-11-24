from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAcknowledgeDeadLetterQueueRecordsRequestEntry(BaseModel):
    ReceiptHandle: StrictStr
