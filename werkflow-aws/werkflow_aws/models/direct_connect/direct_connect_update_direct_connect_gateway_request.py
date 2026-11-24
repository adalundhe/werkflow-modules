from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectUpdateDirectConnectGatewayRequest(BaseModel):
    directConnectGatewayId: StrictStr
    newDirectConnectGatewayName: StrictStr
