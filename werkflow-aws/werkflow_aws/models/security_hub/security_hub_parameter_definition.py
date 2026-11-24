from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_configuration_options import SecurityHubConfigurationOptions


class SecurityHubParameterDefinition(BaseModel):
    Description: StrictStr | None = None
    ConfigurationOptions: SecurityHubConfigurationOptions | None = None
