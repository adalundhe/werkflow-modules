from __future__ import annotations
from pydantic import BaseModel, StrictBool


class GuardDutySecurityContext(BaseModel):
    Privileged: StrictBool | None = None
    AllowPrivilegeEscalation: StrictBool | None = None
