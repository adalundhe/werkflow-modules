from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchAlarmTagsPropagation(BaseModel):
    Enabled: StrictBool | None = None
    IncludedTagKeys: list[StrictStr] | None = None
    ExcludedTagKeys: list[StrictStr] | None = None
