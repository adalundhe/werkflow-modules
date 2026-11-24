from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .elasti_cache_processed_update_action import ElastiCacheProcessedUpdateAction
from .elasti_cache_unprocessed_update_action import ElastiCacheUnprocessedUpdateAction


class ElastiCacheBatchStopUpdateActionResponse(BaseModel):
    ProcessedUpdateActions: list[ElastiCacheProcessedUpdateAction] | None = None
    UnprocessedUpdateActions: list[ElastiCacheUnprocessedUpdateAction] | None = None
    ResponseMetadata: dict[str, Any] | None = None
