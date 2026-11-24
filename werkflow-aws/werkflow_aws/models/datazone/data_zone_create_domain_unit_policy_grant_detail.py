from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneCreateDomainUnitPolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
