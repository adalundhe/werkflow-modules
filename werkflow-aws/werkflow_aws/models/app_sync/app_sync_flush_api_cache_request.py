from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncFlushApiCacheRequest(BaseModel):
    apiId: StrictStr
