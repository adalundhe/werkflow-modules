from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_parameter_name_value import ElastiCacheParameterNameValue


class ElastiCacheResetCacheParameterGroupRequest(BaseModel):
    CacheParameterGroupName: StrictStr
    ResetAllParameters: StrictBool | None = None
    ParameterNameValues: list[ElastiCacheParameterNameValue] | None = None
