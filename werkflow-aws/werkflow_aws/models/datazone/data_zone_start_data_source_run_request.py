from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneStartDataSourceRunRequest(BaseModel):
    domainIdentifier: StrictStr
    dataSourceIdentifier: StrictStr
    clientToken: StrictStr | None = None
