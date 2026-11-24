from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
