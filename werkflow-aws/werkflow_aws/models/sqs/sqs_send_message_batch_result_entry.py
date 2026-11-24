from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSSendMessageBatchResultEntry(BaseModel):
    Id: StrictStr | None = None
    MessageId: StrictStr | None = None
    MD5OfMessageBody: StrictStr | None = None
    MD5OfMessageAttributes: StrictStr | None = None
    MD5OfMessageSystemAttributes: StrictStr | None = None
    SequenceNumber: StrictStr | None = None
