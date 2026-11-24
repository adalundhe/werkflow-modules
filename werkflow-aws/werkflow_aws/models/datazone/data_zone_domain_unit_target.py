from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneDomainUnitTarget(BaseModel):
    domainUnitId: StrictStr | None = None
    includeChildDomainUnits: StrictBool | None = None
