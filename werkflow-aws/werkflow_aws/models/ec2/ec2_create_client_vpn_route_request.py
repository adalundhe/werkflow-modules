from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CreateClientVpnRouteRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    DestinationCidrBlock: StrictStr
    TargetVpcSubnetId: StrictStr | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
