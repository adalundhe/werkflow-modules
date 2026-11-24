from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_pool import EC2IpamPool


class EC2CreateIpamPoolResponse(BaseModel):
    IpamPool: EC2IpamPool | None = None
    ResponseMetadata: dict[str, Any] | None = None
