from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutySecurityGroup(BaseModel):
    GroupId: StrictStr | None = None
    GroupName: StrictStr | None = None
