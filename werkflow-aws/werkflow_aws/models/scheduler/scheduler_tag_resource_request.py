from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .scheduler_tag import SchedulerTag


class SchedulerTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[SchedulerTag]
