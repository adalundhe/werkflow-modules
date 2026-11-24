from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_client_vpn_endpoint_status import EC2ClientVpnEndpointStatus


class EC2CreateClientVpnEndpointResponse(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    Status: EC2ClientVpnEndpointStatus | None = None
    DnsName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
