from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_cache_node_type_specific_parameter import ElastiCacheCacheNodeTypeSpecificParameter
from .elasti_cache_parameter import ElastiCacheParameter


class ElastiCacheEngineDefaults(BaseModel):
    CacheParameterGroupFamily: StrictStr | None = None
    Marker: StrictStr | None = None
    Parameters: list[ElastiCacheParameter] | None = None
    CacheNodeTypeSpecificParameters: list[ElastiCacheCacheNodeTypeSpecificParameter] | None = None
