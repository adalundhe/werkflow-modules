from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpn_connection import EC2VpnConnection


class EC2ModifyVpnConnectionOptionsResponse(BaseModel):
    VpnConnection: EC2VpnConnection | None = None
    ResponseMetadata: dict[str, Any] | None = None
