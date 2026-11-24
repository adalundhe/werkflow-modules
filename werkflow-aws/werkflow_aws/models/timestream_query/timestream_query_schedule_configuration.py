from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryScheduleConfiguration(BaseModel):
    ScheduleExpression: StrictStr | None = None
