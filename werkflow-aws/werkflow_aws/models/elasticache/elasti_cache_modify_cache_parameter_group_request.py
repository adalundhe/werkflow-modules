from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_parameter_name_value import ElastiCacheParameterNameValue


class ElastiCacheModifyCacheParameterGroupRequest(BaseModel):
    CacheParameterGroupName: StrictStr
    ParameterNameValues: list[ElastiCacheParameterNameValue]
