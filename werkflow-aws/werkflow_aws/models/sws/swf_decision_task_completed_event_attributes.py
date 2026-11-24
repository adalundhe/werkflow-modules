from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_task_list import SWFTaskList


class SWFDecisionTaskCompletedEventAttributes(BaseModel):
    executionContext: StrictStr | None = None
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
    taskList: SWFTaskList | None = None
    taskListScheduleToStartTimeout: StrictStr | None = None
