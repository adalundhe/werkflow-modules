from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_remediation_configuration import ConfigServiceRemediationConfiguration


class ConfigServiceDescribeRemediationConfigurationsResponse(BaseModel):
    RemediationConfigurations: list[ConfigServiceRemediationConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
