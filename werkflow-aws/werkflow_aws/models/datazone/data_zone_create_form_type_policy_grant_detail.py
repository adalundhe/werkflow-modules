from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneCreateFormTypePolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
