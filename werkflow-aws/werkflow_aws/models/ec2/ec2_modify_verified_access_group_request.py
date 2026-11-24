from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVerifiedAccessGroupRequest(BaseModel):
    VerifiedAccessGroupId: StrictStr
    VerifiedAccessInstanceId: StrictStr | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
