from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
