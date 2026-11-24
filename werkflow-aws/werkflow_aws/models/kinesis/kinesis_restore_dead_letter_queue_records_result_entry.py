from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisRestoreDeadLetterQueueRecordsResultEntry(BaseModel):
    ReceiptHandle: StrictStr | None = None
