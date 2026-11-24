from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_custom_plugin_configuration import QBusinessCustomPluginConfiguration
from .q_business_plugin_auth_configuration import QBusinessPluginAuthConfiguration


class QBusinessGetPluginResponse(BaseModel):
    applicationId: StrictStr | None = None
    pluginId: StrictStr | None = None
    displayName: StrictStr | None = None
    type: StrictStr | None = None
    serverUrl: StrictStr | None = None
    authConfiguration: QBusinessPluginAuthConfiguration | None = None
    customPluginConfiguration: QBusinessCustomPluginConfiguration | None = None
    buildStatus: StrictStr | None = None
    pluginArn: StrictStr | None = None
    state: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
