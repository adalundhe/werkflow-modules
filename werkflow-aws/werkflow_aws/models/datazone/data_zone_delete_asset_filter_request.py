from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteAssetFilterRequest(BaseModel):
    domainIdentifier: StrictStr
    assetIdentifier: StrictStr
    identifier: StrictStr
