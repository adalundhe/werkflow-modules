from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFActivityTaskTimedOutEventAttributes(BaseModel):
    timeoutType: StrictStr | None = None
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
    details: StrictStr | None = None
