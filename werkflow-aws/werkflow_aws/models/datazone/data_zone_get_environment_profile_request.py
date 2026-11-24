from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetEnvironmentProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
