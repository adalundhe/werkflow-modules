from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteCacheReportRequest(BaseModel):
    CacheReportARN: StrictStr
