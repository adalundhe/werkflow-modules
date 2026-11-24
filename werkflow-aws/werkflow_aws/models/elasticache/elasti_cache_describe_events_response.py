from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_event import ElastiCacheEvent


class ElastiCacheDescribeEventsResponse(BaseModel):
    Marker: StrictStr | None = None
    Events: list[ElastiCacheEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
