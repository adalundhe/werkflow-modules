from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheStopMigrationRequest(BaseModel):
    ServerlessCacheName: StrictStr
