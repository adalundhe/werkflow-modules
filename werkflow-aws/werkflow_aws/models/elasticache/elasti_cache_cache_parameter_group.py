from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ElastiCacheCacheParameterGroup(BaseModel):
    CacheParameterGroupName: StrictStr | None = None
    CacheParameterGroupFamily: StrictStr | None = None
    Description: StrictStr | None = None
    IsGlobal: StrictBool | None = None
    ARN: StrictStr | None = None
