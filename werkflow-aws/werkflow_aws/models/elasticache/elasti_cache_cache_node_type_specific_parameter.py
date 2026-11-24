from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_cache_node_type_specific_value import ElastiCacheCacheNodeTypeSpecificValue


class ElastiCacheCacheNodeTypeSpecificParameter(BaseModel):
    ParameterName: StrictStr | None = None
    Description: StrictStr | None = None
    Source: StrictStr | None = None
    DataType: StrictStr | None = None
    AllowedValues: StrictStr | None = None
    IsModifiable: StrictBool | None = None
    MinimumEngineVersion: StrictStr | None = None
    CacheNodeTypeSpecificValues: list[ElastiCacheCacheNodeTypeSpecificValue] | None = None
    ChangeType: StrictStr | None = None
