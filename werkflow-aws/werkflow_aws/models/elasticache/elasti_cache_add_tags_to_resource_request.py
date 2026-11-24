from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheAddTagsToResourceRequest(BaseModel):
    ResourceName: StrictStr
    Tags: list[ElastiCacheTag]
