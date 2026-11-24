from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_resharding_configuration import ElastiCacheReshardingConfiguration


class ElastiCacheRegionalConfiguration(BaseModel):
    ReplicationGroupId: StrictStr
    ReplicationGroupRegion: StrictStr
    ReshardingConfiguration: list[ElastiCacheReshardingConfiguration]
