from __future__ import annotations
from pydantic import BaseModel
from .q_business_plugin_configuration import QBusinessPluginConfiguration


class QBusinessChatModeConfiguration(BaseModel):
    pluginConfiguration: QBusinessPluginConfiguration | None = None
