from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteLineageEventRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
