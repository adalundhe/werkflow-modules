from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataZoneListDomainUnitsForParentRequest(BaseModel):
    domainIdentifier: StrictStr
    parentDomainUnitIdentifier: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
