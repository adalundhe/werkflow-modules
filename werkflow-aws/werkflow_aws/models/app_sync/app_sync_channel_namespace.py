from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_sync_auth_mode import AppSyncAuthMode
from .app_sync_handler_configs import AppSyncHandlerConfigs


class AppSyncChannelNamespace(BaseModel):
    apiId: StrictStr | None = None
    name: StrictStr | None = None
    subscribeAuthModes: list[AppSyncAuthMode] | None = None
    publishAuthModes: list[AppSyncAuthMode] | None = None
    codeHandlers: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    channelNamespaceArn: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    lastModified: datetime.datetime | StrictStr | None = None
    handlerConfigs: AppSyncHandlerConfigs | None = None
