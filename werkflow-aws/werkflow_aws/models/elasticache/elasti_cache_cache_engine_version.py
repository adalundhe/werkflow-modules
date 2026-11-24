from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheCacheEngineVersion(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    CacheParameterGroupFamily: StrictStr | None = None
    CacheEngineDescription: StrictStr | None = None
    CacheEngineVersionDescription: StrictStr | None = None
