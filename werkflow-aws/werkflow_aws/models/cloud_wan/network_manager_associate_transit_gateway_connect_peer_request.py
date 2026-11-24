from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAssociateTransitGatewayConnectPeerRequest(BaseModel):
    GlobalNetworkId: StrictStr
    TransitGatewayConnectPeerArn: StrictStr
    DeviceId: StrictStr
    LinkId: StrictStr | None = None
