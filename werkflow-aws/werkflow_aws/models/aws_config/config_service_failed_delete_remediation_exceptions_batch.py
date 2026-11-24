from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_remediation_exception_resource_key import ConfigServiceRemediationExceptionResourceKey


class ConfigServiceFailedDeleteRemediationExceptionsBatch(BaseModel):
    FailureMessage: StrictStr | None = None
    FailedItems: list[ConfigServiceRemediationExceptionResourceKey] | None = None
