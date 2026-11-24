from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetDomainRequest(BaseModel):
    identifier: StrictStr
