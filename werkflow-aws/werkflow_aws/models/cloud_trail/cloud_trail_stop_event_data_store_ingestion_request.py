from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStopEventDataStoreIngestionRequest(BaseModel):
    EventDataStore: StrictStr
