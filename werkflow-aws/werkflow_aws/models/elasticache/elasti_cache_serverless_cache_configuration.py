from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheServerlessCacheConfiguration(BaseModel):
    ServerlessCacheName: StrictStr | None = None
    Engine: StrictStr | None = None
    MajorEngineVersion: StrictStr | None = None
