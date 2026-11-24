from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_gcp_configuration_targets import SSMGcpConfigurationTargets


class SSMGcpConfiguration(BaseModel):
    OrganizationId: StrictStr | None = None
    WorkloadIdentityPoolProvider: StrictStr | None = None
    ServiceAccountEmail: StrictStr | None = None
    Targets: SSMGcpConfigurationTargets | None = None
