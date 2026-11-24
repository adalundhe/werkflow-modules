from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteConnectionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
