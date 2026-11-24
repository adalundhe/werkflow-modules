from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_resolver import AppSyncResolver


class AppSyncCreateResolverResponse(BaseModel):
    resolver: AppSyncResolver | None = None
    ResponseMetadata: dict[str, Any] | None = None
