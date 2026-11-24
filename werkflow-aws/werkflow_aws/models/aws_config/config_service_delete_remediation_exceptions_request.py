from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_remediation_exception_resource_key import ConfigServiceRemediationExceptionResourceKey


class ConfigServiceDeleteRemediationExceptionsRequest(BaseModel):
    ConfigRuleName: StrictStr
    ResourceKeys: list[ConfigServiceRemediationExceptionResourceKey]
