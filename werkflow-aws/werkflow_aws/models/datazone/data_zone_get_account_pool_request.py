from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetAccountPoolRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
