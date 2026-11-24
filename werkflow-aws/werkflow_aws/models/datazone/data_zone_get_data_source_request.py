from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetDataSourceRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
