from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteLocalGatewayRouteRequest(BaseModel):
    LocalGatewayRouteTableId: StrictStr
    DestinationCidrBlock: StrictStr | None = None
    DryRun: StrictBool | None = None
    DestinationPrefixListId: StrictStr | None = None
