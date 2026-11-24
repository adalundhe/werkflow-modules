from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AssociateRouteTableRequest(BaseModel):
    RouteTableId: StrictStr
    GatewayId: StrictStr | None = None
    PublicIpv4Pool: StrictStr | None = None
    DryRun: StrictBool | None = None
    SubnetId: StrictStr | None = None
