from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCreateDomainUnitRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    parentDomainUnitIdentifier: StrictStr
    description: StrictStr | None = None
    clientToken: StrictStr | None = None
