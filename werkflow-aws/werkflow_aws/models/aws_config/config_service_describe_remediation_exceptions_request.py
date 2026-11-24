from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_remediation_exception_resource_key import ConfigServiceRemediationExceptionResourceKey


class ConfigServiceDescribeRemediationExceptionsRequest(BaseModel):
    ConfigRuleName: StrictStr
    ResourceKeys: list[ConfigServiceRemediationExceptionResourceKey] | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
