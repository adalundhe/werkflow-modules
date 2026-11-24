from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDomainUnitGroupProperties(BaseModel):
    groupId: StrictStr | None = None
