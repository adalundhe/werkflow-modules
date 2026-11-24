from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetDomainUnitRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
