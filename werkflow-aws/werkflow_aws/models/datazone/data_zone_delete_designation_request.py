from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteDesignationRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
