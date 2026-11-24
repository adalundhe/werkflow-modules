from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheCreateUserGroupRequest(BaseModel):
    UserGroupId: StrictStr
    Engine: StrictStr
    UserIds: list[StrictStr] | None = None
    Tags: list[ElastiCacheTag] | None = None
