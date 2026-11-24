from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetLineageEventRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
