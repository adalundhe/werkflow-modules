from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailStartEventDataStoreIngestionRequest(BaseModel):
    EventDataStore: StrictStr
