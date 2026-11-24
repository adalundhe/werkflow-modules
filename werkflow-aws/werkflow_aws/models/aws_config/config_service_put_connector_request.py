from __future__ import annotations
from pydantic import BaseModel
from .config_service_connector_configuration import ConfigServiceConnectorConfiguration
from .config_service_tag import ConfigServiceTag


class ConfigServicePutConnectorRequest(BaseModel):
    ConnectorConfiguration: ConfigServiceConnectorConfiguration
    Tags: list[ConfigServiceTag] | None = None
