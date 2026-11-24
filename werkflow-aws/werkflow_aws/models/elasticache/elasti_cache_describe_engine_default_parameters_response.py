from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_engine_defaults import ElastiCacheEngineDefaults


class ElastiCacheDescribeEngineDefaultParametersResponse(BaseModel):
    EngineDefaults: ElastiCacheEngineDefaults | None = None
    ResponseMetadata: dict[str, Any] | None = None
