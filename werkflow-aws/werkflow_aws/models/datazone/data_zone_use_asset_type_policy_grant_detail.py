from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUseAssetTypePolicyGrantDetail(BaseModel):
    domainUnitId: StrictStr | None = None
