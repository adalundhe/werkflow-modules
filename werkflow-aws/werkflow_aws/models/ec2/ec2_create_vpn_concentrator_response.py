from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_vpn_concentrator import EC2VpnConcentrator


class EC2CreateVpnConcentratorResponse(BaseModel):
    VpnConcentrator: EC2VpnConcentrator | None = None
    ResponseMetadata: dict[str, Any] | None = None
