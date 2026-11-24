from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayCancelCacheReportRequest(BaseModel):
    CacheReportARN: StrictStr
