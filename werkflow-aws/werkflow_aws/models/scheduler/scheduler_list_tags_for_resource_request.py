from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
