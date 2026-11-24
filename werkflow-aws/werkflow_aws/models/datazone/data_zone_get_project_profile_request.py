from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetProjectProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
