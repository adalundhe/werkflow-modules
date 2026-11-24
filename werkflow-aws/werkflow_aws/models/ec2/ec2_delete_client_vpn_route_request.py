from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteClientVpnRouteRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    DestinationCidrBlock: StrictStr
    TargetVpcSubnetId: StrictStr | None = None
    DryRun: StrictBool | None = None
