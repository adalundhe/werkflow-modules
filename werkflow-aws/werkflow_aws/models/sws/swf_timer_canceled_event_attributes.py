from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFTimerCanceledEventAttributes(BaseModel):
    timerId: StrictStr | None = None
    startedEventId: StrictInt | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
