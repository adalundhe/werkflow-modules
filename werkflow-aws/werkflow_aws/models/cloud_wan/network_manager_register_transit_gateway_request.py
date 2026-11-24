from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRegisterTransitGatewayRequest(BaseModel):
    GlobalNetworkId: StrictStr
    TransitGatewayArn: StrictStr
