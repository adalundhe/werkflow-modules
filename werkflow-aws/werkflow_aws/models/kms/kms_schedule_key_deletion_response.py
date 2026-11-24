from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class KMSScheduleKeyDeletionResponse(BaseModel):
    KeyId: StrictStr | None = None
    DeletionDate: datetime.datetime | StrictStr | None = None
    KeyState: StrictStr | None = None
    PendingWindowInDays: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
