from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAcceptedAssetScope(BaseModel):
    assetId: StrictStr
    filterIds: list[StrictStr]
