from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
