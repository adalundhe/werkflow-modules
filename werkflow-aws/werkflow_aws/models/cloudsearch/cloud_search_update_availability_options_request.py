from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudSearchUpdateAvailabilityOptionsRequest(BaseModel):
    DomainName: StrictStr
    MultiAZ: StrictBool
