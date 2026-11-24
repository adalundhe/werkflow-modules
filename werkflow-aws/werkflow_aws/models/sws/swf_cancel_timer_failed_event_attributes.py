from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFCancelTimerFailedEventAttributes(BaseModel):
    timerId: StrictStr | None = None
    cause: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
