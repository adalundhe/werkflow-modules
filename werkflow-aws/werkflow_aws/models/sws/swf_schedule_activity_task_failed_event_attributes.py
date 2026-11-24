from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_activity_type import SWFActivityType


class SWFScheduleActivityTaskFailedEventAttributes(BaseModel):
    activityType: SWFActivityType | None = None
    activityId: StrictStr | None = None
    cause: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
