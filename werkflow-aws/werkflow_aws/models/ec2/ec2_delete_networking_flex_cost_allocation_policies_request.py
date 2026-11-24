from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteNetworkingFlexCostAllocationPoliciesRequest(BaseModel):
    FcaPolicyIds: list[StrictStr]
    DryRun: StrictBool | None = None
