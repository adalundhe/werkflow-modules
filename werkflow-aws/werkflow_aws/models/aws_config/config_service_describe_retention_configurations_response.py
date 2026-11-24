from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_retention_configuration import ConfigServiceRetentionConfiguration


class ConfigServiceDescribeRetentionConfigurationsResponse(BaseModel):
    RetentionConfigurations: list[ConfigServiceRetentionConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
