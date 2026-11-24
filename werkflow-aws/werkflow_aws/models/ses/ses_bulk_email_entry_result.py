from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESBulkEmailEntryResult(BaseModel):
    Status: StrictStr | None = None
    Error: StrictStr | None = None
    MessageId: StrictStr | None = None
