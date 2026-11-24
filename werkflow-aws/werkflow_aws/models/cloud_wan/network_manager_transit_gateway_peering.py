from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .network_manager_peering import NetworkManagerPeering


class NetworkManagerTransitGatewayPeering(BaseModel):
    Peering: NetworkManagerPeering | None = None
    TransitGatewayArn: StrictStr | None = None
    TransitGatewayPeeringAttachmentId: StrictStr | None = None
