from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteApiCacheRequest(BaseModel):
    apiId: StrictStr
