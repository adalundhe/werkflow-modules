from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisUpdateQueueRecordsVisibilityResultEntry(BaseModel):
    ReceiptHandle: StrictStr | None = None
