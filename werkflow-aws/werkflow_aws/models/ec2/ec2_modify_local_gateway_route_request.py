from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyLocalGatewayRouteRequest(BaseModel):
    LocalGatewayRouteTableId: StrictStr
    DestinationCidrBlock: StrictStr | None = None
    LocalGatewayVirtualInterfaceGroupId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    DryRun: StrictBool | None = None
    DestinationPrefixListId: StrictStr | None = None
