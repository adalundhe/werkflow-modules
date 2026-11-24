from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAcknowledgeDeadLetterQueueRecordsResultEntry(BaseModel):
    ReceiptHandle: StrictStr | None = None
