from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerDisassociateCustomerGatewayRequest(BaseModel):
    GlobalNetworkId: StrictStr
    CustomerGatewayArn: StrictStr
