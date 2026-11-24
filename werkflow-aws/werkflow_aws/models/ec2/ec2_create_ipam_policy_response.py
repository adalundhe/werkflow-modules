from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_policy import EC2IpamPolicy


class EC2CreateIpamPolicyResponse(BaseModel):
    IpamPolicy: EC2IpamPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
