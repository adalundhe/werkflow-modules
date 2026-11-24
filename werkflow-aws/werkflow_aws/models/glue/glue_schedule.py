from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSchedule(BaseModel):
    ScheduleExpression: StrictStr | None = None
    State: StrictStr | None = None
