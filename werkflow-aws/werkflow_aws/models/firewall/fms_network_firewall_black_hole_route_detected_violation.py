from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_route import FMSRoute


class FMSNetworkFirewallBlackHoleRouteDetectedViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    RouteTableId: StrictStr | None = None
    VpcId: StrictStr | None = None
    ViolatingRoutes: list[FMSRoute] | None = None
