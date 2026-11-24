from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_ipam_policy_allocation_rule import EC2IpamPolicyAllocationRule


class EC2IpamPolicyDocument(BaseModel):
    IpamPolicyId: StrictStr | None = None
    Locale: StrictStr | None = None
    ResourceType: StrictStr | None = None
    AllocationRules: list[EC2IpamPolicyAllocationRule] | None = None
