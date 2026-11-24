from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUpdateDomainUnitRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    description: StrictStr | None = None
    name: StrictStr | None = None
