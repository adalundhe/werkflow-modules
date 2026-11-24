from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_resource_key import ConfigServiceResourceKey


class ConfigServiceDescribeRemediationExecutionStatusRequest(BaseModel):
    ConfigRuleName: StrictStr
    ResourceKeys: list[ConfigServiceResourceKey] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
