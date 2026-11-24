from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_flex_cost_allocation_policy_association_description import EC2FlexCostAllocationPolicyAssociationDescription


class EC2DescribeNetworkingFlexCostAllocationPolicyAssociationsResponse(BaseModel):
    FcaPolicyAssociations: list[EC2FlexCostAllocationPolicyAssociationDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
