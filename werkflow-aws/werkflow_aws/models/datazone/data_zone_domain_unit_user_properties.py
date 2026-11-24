from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDomainUnitUserProperties(BaseModel):
    userId: StrictStr | None = None
