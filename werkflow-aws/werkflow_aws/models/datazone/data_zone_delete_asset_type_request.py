from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteAssetTypeRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
