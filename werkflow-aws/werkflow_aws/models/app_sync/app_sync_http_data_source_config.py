from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_authorization_config import AppSyncAuthorizationConfig


class AppSyncHttpDataSourceConfig(BaseModel):
    endpoint: StrictStr | None = None
    authorizationConfig: AppSyncAuthorizationConfig | None = None
