from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_organization_status import NetworkManagerOrganizationStatus


class NetworkManagerListOrganizationServiceAccessStatusResponse(BaseModel):
    OrganizationStatus: NetworkManagerOrganizationStatus | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
