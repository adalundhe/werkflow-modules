from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_scope import EC2IpamScope


class EC2DescribeIpamScopesResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamScopes: list[EC2IpamScope] | None = None
    ResponseMetadata: dict[str, Any] | None = None
