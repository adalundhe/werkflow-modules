from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcBlockPublicAccessExclusionRequest(BaseModel):
    ExclusionId: StrictStr
    DryRun: StrictBool | None = None
