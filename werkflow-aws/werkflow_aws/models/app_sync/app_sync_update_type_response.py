from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_type import AppSyncType


class AppSyncUpdateTypeResponse(BaseModel):
    type: AppSyncType | None = None
    ResponseMetadata: dict[str, Any] | None = None
