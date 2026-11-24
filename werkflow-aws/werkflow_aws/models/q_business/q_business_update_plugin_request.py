from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_custom_plugin_configuration import QBusinessCustomPluginConfiguration
from .q_business_plugin_auth_configuration import QBusinessPluginAuthConfiguration


class QBusinessUpdatePluginRequest(BaseModel):
    applicationId: StrictStr
    pluginId: StrictStr
    displayName: StrictStr | None = None
    state: Literal['ENABLED', 'DISABLED'] | None = None
    serverUrl: StrictStr | None = None
    customPluginConfiguration: QBusinessCustomPluginConfiguration | None = None
    authConfiguration: QBusinessPluginAuthConfiguration | None = None
