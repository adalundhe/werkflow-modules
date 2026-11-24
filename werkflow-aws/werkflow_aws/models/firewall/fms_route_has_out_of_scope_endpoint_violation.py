from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_route import FMSRoute


class FMSRouteHasOutOfScopeEndpointViolation(BaseModel):
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    RouteTableId: StrictStr | None = None
    ViolatingRoutes: list[FMSRoute] | None = None
    SubnetAvailabilityZone: StrictStr | None = None
    SubnetAvailabilityZoneId: StrictStr | None = None
    CurrentFirewallSubnetRouteTable: StrictStr | None = None
    FirewallSubnetId: StrictStr | None = None
    FirewallSubnetRoutes: list[FMSRoute] | None = None
    InternetGatewayId: StrictStr | None = None
    CurrentInternetGatewayRouteTable: StrictStr | None = None
    InternetGatewayRoutes: list[FMSRoute] | None = None
