from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_service_update import ElastiCacheServiceUpdate


class ElastiCacheDescribeServiceUpdatesResponse(BaseModel):
    Marker: StrictStr | None = None
    ServiceUpdates: list[ElastiCacheServiceUpdate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
