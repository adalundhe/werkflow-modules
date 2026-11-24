from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
