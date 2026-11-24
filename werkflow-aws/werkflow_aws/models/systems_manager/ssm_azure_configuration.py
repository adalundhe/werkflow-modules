from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_configuration_targets import SSMConfigurationTargets


class SSMAzureConfiguration(BaseModel):
    TenantId: StrictStr | None = None
    TenantDisplayName: StrictStr | None = None
    ApplicationId: StrictStr | None = None
    ApplicationDisplayName: StrictStr | None = None
    Targets: SSMConfigurationTargets | None = None
