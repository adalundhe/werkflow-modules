from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_resource_key import ConfigServiceResourceKey


class ConfigServiceStartRemediationExecutionRequest(BaseModel):
    ConfigRuleName: StrictStr
    ResourceKeys: list[ConfigServiceResourceKey]
