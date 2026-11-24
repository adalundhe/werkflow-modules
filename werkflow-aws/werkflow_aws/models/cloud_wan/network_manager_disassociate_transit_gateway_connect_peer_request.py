from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDisassociateTransitGatewayConnectPeerRequest(BaseModel):
    GlobalNetworkId: StrictStr
    TransitGatewayConnectPeerArn: StrictStr
