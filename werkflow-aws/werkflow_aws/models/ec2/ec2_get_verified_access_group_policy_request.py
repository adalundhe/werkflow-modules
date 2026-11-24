from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2GetVerifiedAccessGroupPolicyRequest(BaseModel):
    VerifiedAccessGroupId: StrictStr
    DryRun: StrictBool | None = None
