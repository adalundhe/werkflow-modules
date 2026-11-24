from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDomainUnitSummary(BaseModel):
    name: StrictStr | None = None
    id: StrictStr | None = None
