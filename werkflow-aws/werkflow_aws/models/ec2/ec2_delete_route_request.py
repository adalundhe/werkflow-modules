from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteRouteRequest(BaseModel):
    RouteTableId: StrictStr
    DestinationPrefixListId: StrictStr | None = None
    DryRun: StrictBool | None = None
    DestinationCidrBlock: StrictStr | None = None
    DestinationIpv6CidrBlock: StrictStr | None = None
