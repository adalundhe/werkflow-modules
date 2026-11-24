from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_policy_document import EC2IpamPolicyDocument


class EC2GetIpamPolicyAllocationRulesResponse(BaseModel):
    IpamPolicyDocuments: list[EC2IpamPolicyDocument] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
