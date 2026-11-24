from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_tag import ElastiCacheTag


class ElastiCacheAddTagsToResourceResponse(BaseModel):
    TagList: list[ElastiCacheTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
