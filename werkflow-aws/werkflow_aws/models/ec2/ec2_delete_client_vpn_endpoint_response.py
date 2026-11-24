from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_client_vpn_endpoint_status import EC2ClientVpnEndpointStatus


class EC2DeleteClientVpnEndpointResponse(BaseModel):
    Status: EC2ClientVpnEndpointStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
