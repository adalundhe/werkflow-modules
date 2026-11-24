from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_dhcp_options import EC2DhcpOptions


class EC2CreateDhcpOptionsResponse(BaseModel):
    DhcpOptions: EC2DhcpOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
