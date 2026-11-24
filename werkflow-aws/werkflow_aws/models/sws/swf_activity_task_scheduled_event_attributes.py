from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_activity_type import SWFActivityType
from .swf_task_list import SWFTaskList


class SWFActivityTaskScheduledEventAttributes(BaseModel):
    activityType: SWFActivityType | None = None
    activityId: StrictStr | None = None
    input: StrictStr | None = None
    control: StrictStr | None = None
    scheduleToStartTimeout: StrictStr | None = None
    scheduleToCloseTimeout: StrictStr | None = None
    startToCloseTimeout: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    heartbeatTimeout: StrictStr | None = None
