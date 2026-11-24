from __future__ import annotations
from pydantic import BaseModel
from .config_service_azure_connector_configuration import ConfigServiceAzureConnectorConfiguration
from .config_service_gcp_connector_configuration import ConfigServiceGcpConnectorConfiguration


class ConfigServiceConnectorConfiguration(BaseModel):
    azure: ConfigServiceAzureConnectorConfiguration | None = None
    gcp: ConfigServiceGcpConnectorConfiguration | None = None
