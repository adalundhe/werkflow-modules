from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ElastiCacheDescribeCacheEngineVersionsRequest(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    CacheParameterGroupFamily: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
    DefaultOnly: StrictBool | None = None
