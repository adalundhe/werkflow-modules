from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_flex_cost_allocation_policy_version import EC2FlexCostAllocationPolicyVersion


class EC2GetNetworkingFlexCostAllocationPolicyVersionsResponse(BaseModel):
    FcaPolicyVersions: list[EC2FlexCostAllocationPolicyVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
