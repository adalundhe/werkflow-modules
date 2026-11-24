from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_flex_cost_allocation_policy_description import EC2FlexCostAllocationPolicyDescription


class EC2DescribeNetworkingFlexCostAllocationPoliciesResponse(BaseModel):
    FlexCostAllocationPolicies: list[EC2FlexCostAllocationPolicyDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
