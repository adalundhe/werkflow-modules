from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_auth_mode import AppSyncAuthMode
from .app_sync_handler_configs import AppSyncHandlerConfigs


class AppSyncCreateChannelNamespaceRequest(BaseModel):
    apiId: StrictStr
    name: StrictStr
    subscribeAuthModes: list[AppSyncAuthMode] | None = None
    publishAuthModes: list[AppSyncAuthMode] | None = None
    codeHandlers: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    handlerConfigs: AppSyncHandlerConfigs | None = None
