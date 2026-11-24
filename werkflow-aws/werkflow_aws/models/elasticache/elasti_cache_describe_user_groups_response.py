from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_user_group import ElastiCacheUserGroup


class ElastiCacheDescribeUserGroupsResponse(BaseModel):
    UserGroups: list[ElastiCacheUserGroup] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
