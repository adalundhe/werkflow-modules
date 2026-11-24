from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_connection import EC2ClientVpnConnection


class EC2DescribeClientVpnConnectionsResponse(BaseModel):
    Connections: list[EC2ClientVpnConnection] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
