from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_flex_cost_allocation_operation_failure import EC2FlexCostAllocationOperationFailure


class EC2DeleteNetworkingFlexCostAllocationPoliciesResponse(BaseModel):
    Successful: list[StrictStr] | None = None
    Failed: list[EC2FlexCostAllocationOperationFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
