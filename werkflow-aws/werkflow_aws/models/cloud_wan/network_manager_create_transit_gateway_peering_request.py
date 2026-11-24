from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_tag import NetworkManagerTag


class NetworkManagerCreateTransitGatewayPeeringRequest(BaseModel):
    CoreNetworkId: StrictStr
    TransitGatewayArn: StrictStr
    Tags: list[NetworkManagerTag] | None = None
    ClientToken: StrictStr | None = None
