from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailRestoreEventDataStoreRequest(BaseModel):
    EventDataStore: StrictStr
