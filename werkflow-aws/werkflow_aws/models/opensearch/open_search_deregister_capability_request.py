from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeregisterCapabilityRequest(BaseModel):
    applicationId: StrictStr
    capabilityName: StrictStr
