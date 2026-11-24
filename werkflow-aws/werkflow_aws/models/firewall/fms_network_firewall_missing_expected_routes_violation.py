from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_expected_route import FMSExpectedRoute


class FMSNetworkFirewallMissingExpectedRoutesViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    ExpectedRoutes: list[FMSExpectedRoute] | None = None
    VpcId: StrictStr | None = None
