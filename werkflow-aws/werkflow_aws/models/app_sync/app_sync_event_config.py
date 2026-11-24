from __future__ import annotations
from pydantic import BaseModel
from .app_sync_auth_mode import AppSyncAuthMode
from .app_sync_auth_provider import AppSyncAuthProvider
from .app_sync_event_log_config import AppSyncEventLogConfig


class AppSyncEventConfig(BaseModel):
    authProviders: list[AppSyncAuthProvider] | None = None
    connectionAuthModes: list[AppSyncAuthMode] | None = None
    defaultPublishAuthModes: list[AppSyncAuthMode] | None = None
    defaultSubscribeAuthModes: list[AppSyncAuthMode] | None = None
    logConfig: AppSyncEventLogConfig | None = None
