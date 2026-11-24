from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFTimerStartedEventAttributes(BaseModel):
    timerId: StrictStr | None = None
    control: StrictStr | None = None
    startToFireTimeout: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
