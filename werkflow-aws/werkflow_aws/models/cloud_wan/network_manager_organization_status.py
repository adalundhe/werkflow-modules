from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_account_status import NetworkManagerAccountStatus


class NetworkManagerOrganizationStatus(BaseModel):
    OrganizationId: StrictStr | None = None
    OrganizationAwsServiceAccessStatus: StrictStr | None = None
    SLRDeploymentStatus: StrictStr | None = None
    AccountStatusList: list[NetworkManagerAccountStatus] | None = None
