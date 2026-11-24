from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2TransitGatewayMulticastRegisteredGroupSources(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr | None = None
    RegisteredNetworkInterfaceIds: list[StrictStr] | None = None
    GroupIpAddress: StrictStr | None = None
