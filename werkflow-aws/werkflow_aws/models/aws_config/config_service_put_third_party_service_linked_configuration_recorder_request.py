from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_scope_configuration import ConfigServiceScopeConfiguration
from .config_service_tag import ConfigServiceTag


class ConfigServicePutThirdPartyServiceLinkedConfigurationRecorderRequest(BaseModel):
    ServicePrincipal: StrictStr
    ConnectorArn: StrictStr
    ScopeConfiguration: ConfigServiceScopeConfiguration
    Tags: list[ConfigServiceTag] | None = None
