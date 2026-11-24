from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_type import AppSyncType


class AppSyncListTypesResponse(BaseModel):
    types: list[AppSyncType] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
