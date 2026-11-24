from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
    expectedVersion: StrictInt | None = None
