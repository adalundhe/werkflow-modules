from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_transit_gateway_registration_state_reason import NetworkManagerTransitGatewayRegistrationStateReason


class NetworkManagerTransitGatewayRegistration(BaseModel):
    GlobalNetworkId: StrictStr | None = None
    TransitGatewayArn: StrictStr | None = None
    State: NetworkManagerTransitGatewayRegistrationStateReason | None = None
