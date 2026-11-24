from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RDSModifyActivityStreamRequest(BaseModel):
    ResourceArn: StrictStr | None = None
    AuditPolicyState: Literal['locked', 'unlocked'] | None = None
