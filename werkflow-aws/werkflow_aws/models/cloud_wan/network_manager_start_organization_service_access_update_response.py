from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .network_manager_organization_status import NetworkManagerOrganizationStatus


class NetworkManagerStartOrganizationServiceAccessUpdateResponse(BaseModel):
    OrganizationStatus: NetworkManagerOrganizationStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
