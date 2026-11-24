from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_transit_gateway_registration import NetworkManagerTransitGatewayRegistration


class NetworkManagerGetTransitGatewayRegistrationsResponse(BaseModel):
    TransitGatewayRegistrations: list[NetworkManagerTransitGatewayRegistration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
