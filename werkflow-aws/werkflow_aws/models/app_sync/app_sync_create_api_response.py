from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_api import AppSyncApi


class AppSyncCreateApiResponse(BaseModel):
    api: AppSyncApi | None = None
    ResponseMetadata: dict[str, Any] | None = None
