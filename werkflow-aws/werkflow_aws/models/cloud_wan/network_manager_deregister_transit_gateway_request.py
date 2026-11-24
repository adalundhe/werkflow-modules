from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDeregisterTransitGatewayRequest(BaseModel):
    GlobalNetworkId: StrictStr
    TransitGatewayArn: StrictStr
