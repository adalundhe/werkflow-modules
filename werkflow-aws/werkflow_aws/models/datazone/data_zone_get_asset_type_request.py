from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetAssetTypeRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    revision: StrictStr | None = None
