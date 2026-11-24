from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteAccountPoolRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
