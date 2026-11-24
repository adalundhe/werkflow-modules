from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneDomainUnitFilterForProject(BaseModel):
    domainUnit: StrictStr | None = None
    includeChildDomainUnits: StrictBool | None = None
