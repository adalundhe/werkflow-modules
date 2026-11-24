from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_update_action import ElastiCacheUpdateAction


class ElastiCacheDescribeUpdateActionsResponse(BaseModel):
    Marker: StrictStr | None = None
    UpdateActions: list[ElastiCacheUpdateAction] | None = None
    ResponseMetadata: dict[str, Any] | None = None
