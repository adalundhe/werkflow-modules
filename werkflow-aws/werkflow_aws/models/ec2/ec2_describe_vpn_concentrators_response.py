from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_vpn_concentrator import EC2VpnConcentrator


class EC2DescribeVpnConcentratorsResponse(BaseModel):
    VpnConcentrators: list[EC2VpnConcentrator] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
