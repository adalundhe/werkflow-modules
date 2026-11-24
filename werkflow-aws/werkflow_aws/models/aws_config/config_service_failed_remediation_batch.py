from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_remediation_configuration import ConfigServiceRemediationConfiguration


class ConfigServiceFailedRemediationBatch(BaseModel):
    FailureMessage: StrictStr | None = None
    FailedItems: list[ConfigServiceRemediationConfiguration] | None = None
