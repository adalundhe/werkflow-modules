from __future__ import annotations
from pydantic import BaseModel
from .app_sync_handler_config import AppSyncHandlerConfig


class AppSyncHandlerConfigs(BaseModel):
    onPublish: AppSyncHandlerConfig | None = None
    onSubscribe: AppSyncHandlerConfig | None = None
