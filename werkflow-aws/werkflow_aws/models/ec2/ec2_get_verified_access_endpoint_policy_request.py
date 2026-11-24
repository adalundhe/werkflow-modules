from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetVerifiedAccessEndpointPolicyRequest(BaseModel):
    VerifiedAccessEndpointId: StrictStr
    DryRun: StrictBool | None = None
