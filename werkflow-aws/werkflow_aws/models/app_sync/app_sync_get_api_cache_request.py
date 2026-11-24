from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetApiCacheRequest(BaseModel):
    apiId: StrictStr
