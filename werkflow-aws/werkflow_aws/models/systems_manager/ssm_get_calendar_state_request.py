from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetCalendarStateRequest(BaseModel):
    CalendarNames: list[StrictStr]
    AtTime: StrictStr | None = None
