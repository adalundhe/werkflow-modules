from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAcknowledgeQueueRecordsResultEntry(BaseModel):
    ReceiptHandle: StrictStr | None = None
