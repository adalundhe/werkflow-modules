from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpn_gateway import EC2VpnGateway


class EC2DescribeVpnGatewaysResponse(BaseModel):
    VpnGateways: list[EC2VpnGateway] | None = None
    ResponseMetadata: dict[str, Any] | None = None
