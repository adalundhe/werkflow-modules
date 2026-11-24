from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_subnet import ElastiCacheSubnet


class ElastiCacheCacheSubnetGroup(BaseModel):
    CacheSubnetGroupName: StrictStr | None = None
    CacheSubnetGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    Subnets: list[ElastiCacheSubnet] | None = None
    ARN: StrictStr | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
