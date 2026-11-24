from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneOverrideDomainUnitOwnersPolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
