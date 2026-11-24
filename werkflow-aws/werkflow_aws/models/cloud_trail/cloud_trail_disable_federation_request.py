from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDisableFederationRequest(BaseModel):
    EventDataStore: StrictStr
