from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_endpoint import EC2ClientVpnEndpoint


class EC2DescribeClientVpnEndpointsResponse(BaseModel):
    ClientVpnEndpoints: list[EC2ClientVpnEndpoint] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
