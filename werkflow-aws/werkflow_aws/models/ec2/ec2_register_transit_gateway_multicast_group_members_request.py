from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RegisterTransitGatewayMulticastGroupMembersRequest(BaseModel):
    TransitGatewayMulticastDomainId: StrictStr
    NetworkInterfaceIds: list[StrictStr]
    GroupIpAddress: StrictStr | None = None
    DryRun: StrictBool | None = None
