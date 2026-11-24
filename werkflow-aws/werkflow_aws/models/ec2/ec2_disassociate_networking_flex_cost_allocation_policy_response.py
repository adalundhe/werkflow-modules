from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_flex_cost_allocation_operation_failure import EC2FlexCostAllocationOperationFailure


class EC2DisassociateNetworkingFlexCostAllocationPolicyResponse(BaseModel):
    FcaPolicyDisassociations: list[StrictStr] | None = None
    FcaPolicyDisassociationFailures: list[EC2FlexCostAllocationOperationFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
