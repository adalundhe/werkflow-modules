from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetDataSourceRunRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
