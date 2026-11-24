from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_user import ElastiCacheUser


class ElastiCacheDescribeUsersResponse(BaseModel):
    Users: list[ElastiCacheUser] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
