from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFActivityTaskCompletedEventAttributes(BaseModel):
    result: StrictStr | None = None
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
