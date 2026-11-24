from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheModifyCacheSubnetGroupRequest(BaseModel):
    CacheSubnetGroupName: StrictStr
    CacheSubnetGroupDescription: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
