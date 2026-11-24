from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_route import FMSRoute


class FMSNetworkFirewallUnexpectedFirewallRoutesViolation(BaseModel):
    FirewallSubnetId: StrictStr | None = None
    ViolatingRoutes: list[FMSRoute] | None = None
    RouteTableId: StrictStr | None = None
    FirewallEndpoint: StrictStr | None = None
    VpcId: StrictStr | None = None
