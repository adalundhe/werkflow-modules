from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncCachingConfig(BaseModel):
    ttl: StrictInt | None = None
    cachingKeys: list[StrictStr] | None = None
