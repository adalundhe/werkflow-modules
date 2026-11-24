from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_api_key import AppSyncApiKey


class AppSyncUpdateApiKeyResponse(BaseModel):
    apiKey: AppSyncApiKey | None = None
    ResponseMetadata: dict[str, Any] | None = None
