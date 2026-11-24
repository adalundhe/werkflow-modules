from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVerifiedAccessInstanceRequest(BaseModel):
    VerifiedAccessInstanceId: StrictStr
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
