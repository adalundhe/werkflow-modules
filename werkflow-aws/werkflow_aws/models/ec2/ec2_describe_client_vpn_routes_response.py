from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_route import EC2ClientVpnRoute


class EC2DescribeClientVpnRoutesResponse(BaseModel):
    Routes: list[EC2ClientVpnRoute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
