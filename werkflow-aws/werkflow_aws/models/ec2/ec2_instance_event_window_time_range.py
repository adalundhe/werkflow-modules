from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InstanceEventWindowTimeRange(BaseModel):
    StartWeekDay: StrictStr | None = None
    StartHour: StrictInt | None = None
    EndWeekDay: StrictStr | None = None
    EndHour: StrictInt | None = None
