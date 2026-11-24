from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
