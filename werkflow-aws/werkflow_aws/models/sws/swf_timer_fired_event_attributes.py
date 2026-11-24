from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFTimerFiredEventAttributes(BaseModel):
    timerId: StrictStr | None = None
    startedEventId: StrictInt | None = None
