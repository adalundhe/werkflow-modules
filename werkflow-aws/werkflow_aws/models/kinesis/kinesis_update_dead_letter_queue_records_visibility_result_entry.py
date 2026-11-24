from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisUpdateDeadLetterQueueRecordsVisibilityResultEntry(BaseModel):
    ReceiptHandle: StrictStr | None = None
