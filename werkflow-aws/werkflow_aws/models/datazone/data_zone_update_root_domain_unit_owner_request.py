from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUpdateRootDomainUnitOwnerRequest(BaseModel):
    domainIdentifier: StrictStr
    currentOwner: StrictStr
    newOwner: StrictStr
    clientToken: StrictStr | None = None
