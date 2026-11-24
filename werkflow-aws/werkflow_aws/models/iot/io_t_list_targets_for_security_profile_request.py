from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListTargetsForSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
