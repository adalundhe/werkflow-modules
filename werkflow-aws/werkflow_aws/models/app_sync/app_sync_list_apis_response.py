from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_api import AppSyncApi


class AppSyncListApisResponse(BaseModel):
    apis: list[AppSyncApi] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
