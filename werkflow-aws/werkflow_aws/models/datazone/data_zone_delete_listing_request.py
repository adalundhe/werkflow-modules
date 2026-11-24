from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteListingRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
