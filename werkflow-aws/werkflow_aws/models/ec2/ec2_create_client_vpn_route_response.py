from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_client_vpn_route_status import EC2ClientVpnRouteStatus


class EC2CreateClientVpnRouteResponse(BaseModel):
    Status: EC2ClientVpnRouteStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
