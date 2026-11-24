from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_api_cache import AppSyncApiCache


class AppSyncGetApiCacheResponse(BaseModel):
    apiCache: AppSyncApiCache | None = None
    ResponseMetadata: dict[str, Any] | None = None
