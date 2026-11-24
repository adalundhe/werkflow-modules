from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDeleteEventDataStoreRequest(BaseModel):
    EventDataStore: StrictStr
