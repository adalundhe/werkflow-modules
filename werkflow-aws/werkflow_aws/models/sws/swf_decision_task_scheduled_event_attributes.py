from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFDecisionTaskScheduledEventAttributes(BaseModel):
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    startToCloseTimeout: StrictStr | None = None
    scheduleToStartTimeout: StrictStr | None = None
