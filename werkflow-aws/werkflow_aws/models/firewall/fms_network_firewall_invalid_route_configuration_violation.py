from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_expected_route import FMSExpectedRoute
from .fms_route import FMSRoute


class FMSNetworkFirewallInvalidRouteConfigurationViolation(BaseModel):
    AffectedSubnets: list[StrictStr] | None = None
    RouteTableId: StrictStr | None = None
    IsRouteTableUsedInDifferentAZ: StrictBool | None = None
    ViolatingRoute: FMSRoute | None = None
    CurrentFirewallSubnetRouteTable: StrictStr | None = None
    ExpectedFirewallEndpoint: StrictStr | None = None
    ActualFirewallEndpoint: StrictStr | None = None
    ExpectedFirewallSubnetId: StrictStr | None = None
    ActualFirewallSubnetId: StrictStr | None = None
    ExpectedFirewallSubnetRoutes: list[FMSExpectedRoute] | None = None
    ActualFirewallSubnetRoutes: list[FMSRoute] | None = None
    InternetGatewayId: StrictStr | None = None
    CurrentInternetGatewayRouteTable: StrictStr | None = None
    ExpectedInternetGatewayRoutes: list[FMSExpectedRoute] | None = None
    ActualInternetGatewayRoutes: list[FMSRoute] | None = None
    VpcId: StrictStr | None = None
