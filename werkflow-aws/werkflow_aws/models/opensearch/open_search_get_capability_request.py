from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetCapabilityRequest(BaseModel):
    applicationId: StrictStr
    capabilityName: StrictStr
