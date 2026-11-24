from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFActivityTaskCanceledEventAttributes(BaseModel):
    details: StrictStr | None = None
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
    latestCancelRequestedEventId: StrictInt | None = None
