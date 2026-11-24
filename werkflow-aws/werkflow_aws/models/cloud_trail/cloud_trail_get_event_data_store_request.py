from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailGetEventDataStoreRequest(BaseModel):
    EventDataStore: StrictStr
