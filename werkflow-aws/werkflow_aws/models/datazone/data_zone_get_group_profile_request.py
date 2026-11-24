from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetGroupProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    groupIdentifier: StrictStr
