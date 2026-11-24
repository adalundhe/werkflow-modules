from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_remediation_exception_resource_key import ConfigServiceRemediationExceptionResourceKey


class ConfigServicePutRemediationExceptionsRequest(BaseModel):
    ConfigRuleName: StrictStr
    ResourceKeys: list[ConfigServiceRemediationExceptionResourceKey]
    Message: StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
