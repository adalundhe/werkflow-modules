from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_policy_organization_target import EC2IpamPolicyOrganizationTarget


class EC2GetIpamPolicyOrganizationTargetsResponse(BaseModel):
    OrganizationTargets: list[EC2IpamPolicyOrganizationTarget] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
