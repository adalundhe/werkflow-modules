from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_api_key import AppSyncApiKey


class AppSyncListApiKeysResponse(BaseModel):
    apiKeys: list[AppSyncApiKey] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
