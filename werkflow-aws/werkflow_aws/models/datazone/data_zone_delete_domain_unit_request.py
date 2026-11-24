from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteDomainUnitRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
