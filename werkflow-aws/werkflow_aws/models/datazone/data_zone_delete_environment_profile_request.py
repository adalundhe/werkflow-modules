from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteEnvironmentProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
