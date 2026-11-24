from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayMulticastDeregisteredGroupMembers(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr | None = None
    DeregisteredNetworkInterfaceIds: list[StrictStr] | None = None
    GroupIpAddress: StrictStr | None = None
