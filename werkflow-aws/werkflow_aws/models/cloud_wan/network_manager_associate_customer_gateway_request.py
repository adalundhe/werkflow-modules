from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAssociateCustomerGatewayRequest(BaseModel):
    CustomerGatewayArn: StrictStr
    GlobalNetworkId: StrictStr
    DeviceId: StrictStr
    LinkId: StrictStr | None = None
