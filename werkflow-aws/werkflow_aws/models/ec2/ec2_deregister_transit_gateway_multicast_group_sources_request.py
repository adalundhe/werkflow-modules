from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeregisterTransitGatewayMulticastGroupSourcesRequest(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr | None = None
    GroupIpAddress: StrictStr | None = None
    NetworkInterfaceIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
