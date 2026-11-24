from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVerifiedAccessGroupRequest(BaseModel):
    VerifiedAccessGroupId: StrictStr
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
