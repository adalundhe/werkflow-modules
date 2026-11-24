from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteSecurityGroupRequest(BaseModel):
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
    DryRun: StrictBool | None = None
