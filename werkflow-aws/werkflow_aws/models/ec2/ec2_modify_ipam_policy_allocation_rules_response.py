from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_ipam_policy_document import EC2IpamPolicyDocument


class EC2ModifyIpamPolicyAllocationRulesResponse(BaseModel):
    IpamPolicyDocument: EC2IpamPolicyDocument | None = None
    ResponseMetadata: dict[str, Any] | None = None
