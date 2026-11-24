from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUpdateAssetOwnerRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    targetProjectIdentifier: StrictStr
    clientToken: StrictStr | None = None
