from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAssetTargetNameMap(BaseModel):
    assetId: StrictStr
    targetName: StrictStr
