from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_route_protection_finding import EC2IpamRouteProtectionFinding


class EC2GetIpamRouteProtectionFindingsResponse(BaseModel):
    IpamId: StrictStr | None = None
    RouteProtectionFindings: list[EC2IpamRouteProtectionFinding] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
