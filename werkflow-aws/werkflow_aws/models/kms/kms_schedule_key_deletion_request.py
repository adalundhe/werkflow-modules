from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KMSScheduleKeyDeletionRequest(BaseModel):
    KeyId: StrictStr
    PendingWindowInDays: StrictInt | None = None
