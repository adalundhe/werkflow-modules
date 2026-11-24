from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailEnableFederationRequest(BaseModel):
    EventDataStore: StrictStr
    FederationRoleArn: StrictStr
