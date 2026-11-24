from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_scope import EC2IpamScope


class EC2DeleteIpamScopeResponse(BaseModel):
    IpamScope: EC2IpamScope | None = None
    ResponseMetadata: dict[str, Any] | None = None
