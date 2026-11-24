from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_remediation_exception import ConfigServiceRemediationException


class ConfigServiceFailedRemediationExceptionBatch(BaseModel):
    FailureMessage: StrictStr | None = None
    FailedItems: list[ConfigServiceRemediationException] | None = None
