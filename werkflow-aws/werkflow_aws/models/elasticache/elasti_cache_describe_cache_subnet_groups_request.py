from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheDescribeCacheSubnetGroupsRequest(BaseModel):
    CacheSubnetGroupName: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
