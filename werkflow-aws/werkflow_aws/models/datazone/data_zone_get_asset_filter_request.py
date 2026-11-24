from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetAssetFilterRequest(BaseModel):
    domainIdentifier: StrictStr
    assetIdentifier: StrictStr
    identifier: StrictStr
