from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchMuteTargets(BaseModel):
    AlarmNames: list[StrictStr] | None = None
