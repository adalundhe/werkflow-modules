from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerRole(BaseModel):
    roleType: StrictStr | None = None
    roleArn: StrictStr | None = None
