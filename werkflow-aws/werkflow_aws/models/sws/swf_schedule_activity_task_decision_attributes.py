from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_activity_type import SWFActivityType
from .swf_task_list import SWFTaskList


class SWFScheduleActivityTaskDecisionAttributes(BaseModel):
    activityType: SWFActivityType
    activityId: StrictStr
    control: StrictStr | None = None
    input: StrictStr | None = None
    scheduleToCloseTimeout: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    scheduleToStartTimeout: StrictStr | None = None
    startToCloseTimeout: StrictStr | None = None
    heartbeatTimeout: StrictStr | None = None
