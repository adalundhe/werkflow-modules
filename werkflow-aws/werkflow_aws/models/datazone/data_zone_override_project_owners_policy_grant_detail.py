from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneOverrideProjectOwnersPolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
