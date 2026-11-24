from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisassociateNetworkingFlexCostAllocationPolicyRequest(BaseModel):
    FcaPolicyAssociationIds: list[StrictStr]
    DryRun: StrictBool | None = None
