from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisRestoreDeadLetterQueueRecordsRequestEntry(BaseModel):
    ReceiptHandle: StrictStr
