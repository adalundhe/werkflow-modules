from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteDataProductRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
