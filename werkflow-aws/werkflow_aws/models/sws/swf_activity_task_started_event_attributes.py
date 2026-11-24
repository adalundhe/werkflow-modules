from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFActivityTaskStartedEventAttributes(BaseModel):
    identity: StrictStr | None = None
    scheduledEventId: StrictInt | None = None
