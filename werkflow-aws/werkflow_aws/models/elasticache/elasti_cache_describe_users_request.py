from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .elasti_cache_filter import ElastiCacheFilter


class ElastiCacheDescribeUsersRequest(BaseModel):
    Engine: StrictStr | None = None
    UserId: StrictStr | None = None
    Filters: list[ElastiCacheFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
