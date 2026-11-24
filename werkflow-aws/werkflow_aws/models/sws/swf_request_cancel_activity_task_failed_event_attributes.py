from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFRequestCancelActivityTaskFailedEventAttributes(BaseModel):
    activityId: StrictStr | None = None
    cause: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
