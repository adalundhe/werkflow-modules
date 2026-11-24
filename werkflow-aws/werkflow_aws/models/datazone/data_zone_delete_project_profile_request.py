from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteProjectProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
