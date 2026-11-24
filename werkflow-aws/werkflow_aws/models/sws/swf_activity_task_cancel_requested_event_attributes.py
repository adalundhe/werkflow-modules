from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFActivityTaskCancelRequestedEventAttributes(BaseModel):
    decisionTaskCompletedEventId: StrictInt | None = None
    activityId: StrictStr | None = None
