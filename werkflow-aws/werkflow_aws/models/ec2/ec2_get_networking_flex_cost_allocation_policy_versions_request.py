from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetNetworkingFlexCostAllocationPolicyVersionsRequest(BaseModel):
    FcaPolicyId: StrictStr
    VersionsToInclude: list[StrictInt] | None = None
    DryRun: StrictBool | None = None
