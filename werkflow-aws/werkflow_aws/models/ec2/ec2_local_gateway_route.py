from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2LocalGatewayRoute(BaseModel):
    DestinationCidrBlock: StrictStr | None = None
    LocalGatewayVirtualInterfaceGroupId: StrictStr | None = None
    Type: StrictStr | None = None
    State: StrictStr | None = None
    LocalGatewayRouteTableId: StrictStr | None = None
    LocalGatewayRouteTableArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    CoipPoolId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    DestinationPrefixListId: StrictStr | None = None
