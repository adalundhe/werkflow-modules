from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDeleteControlRequest(BaseModel):
    controlId: StrictStr
