from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_policy import EC2IpamPolicy


class EC2DescribeIpamPoliciesResponse(BaseModel):
    NextToken: StrictStr | None = None
    IpamPolicies: list[EC2IpamPolicy] | None = None
    ResponseMetadata: dict[str, Any] | None = None
