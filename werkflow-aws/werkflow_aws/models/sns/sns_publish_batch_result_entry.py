from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSPublishBatchResultEntry(BaseModel):
    Id: StrictStr | None = None
    MessageId: StrictStr | None = None
    SequenceNumber: StrictStr | None = None
