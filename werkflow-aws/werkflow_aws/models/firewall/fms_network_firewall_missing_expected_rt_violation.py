from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSNetworkFirewallMissingExpectedRTViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    VPC: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    CurrentRouteTable: StrictStr | None = None
    ExpectedRouteTable: StrictStr | None = None
