from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAccountPoolSummary(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    resolutionStrategy: StrictStr | None = None
    domainUnitId: StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedBy: StrictStr | None = None
