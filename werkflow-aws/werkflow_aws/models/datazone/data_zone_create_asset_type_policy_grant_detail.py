from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneCreateAssetTypePolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
