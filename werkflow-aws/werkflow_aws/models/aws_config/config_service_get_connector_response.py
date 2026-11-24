from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_connector import ConfigServiceConnector


class ConfigServiceGetConnectorResponse(BaseModel):
    Connector: ConfigServiceConnector | None = None
    ResponseMetadata: dict[str, Any] | None = None
