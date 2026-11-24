from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_flex_cost_allocation_operation_failure import EC2FlexCostAllocationOperationFailure
from .ec2_flex_cost_allocation_policy_association_description import EC2FlexCostAllocationPolicyAssociationDescription


class EC2AssociateNetworkingFlexCostAllocationPolicyResponse(BaseModel):
    FcaPolicyAssociations: list[EC2FlexCostAllocationPolicyAssociationDescription] | None = None
    FcaPolicyAssociationFailures: list[EC2FlexCostAllocationOperationFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
