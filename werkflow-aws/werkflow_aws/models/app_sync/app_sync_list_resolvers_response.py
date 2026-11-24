from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_resolver import AppSyncResolver


class AppSyncListResolversResponse(BaseModel):
    resolvers: list[AppSyncResolver] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
