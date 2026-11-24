from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_schedule import CloudWatchSchedule


class CloudWatchRule(BaseModel):
    Schedule: CloudWatchSchedule | None = None
