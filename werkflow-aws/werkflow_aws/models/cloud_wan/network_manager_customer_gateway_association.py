from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerCustomerGatewayAssociation(BaseModel):
    CustomerGatewayArn: StrictStr | None = None
    GlobalNetworkId: StrictStr | None = None
    DeviceId: StrictStr | None = None
    LinkId: StrictStr | None = None
    State: StrictStr | None = None
