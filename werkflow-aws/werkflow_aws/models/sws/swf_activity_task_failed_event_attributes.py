from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFActivityTaskFailedEventAttributes(BaseModel):
    reason: StrictStr | None = None
    details: StrictStr | None = None
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
