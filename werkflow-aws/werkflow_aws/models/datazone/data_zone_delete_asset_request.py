from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteAssetRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
