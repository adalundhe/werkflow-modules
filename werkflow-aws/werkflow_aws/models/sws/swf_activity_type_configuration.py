from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFActivityTypeConfiguration(BaseModel):
    defaultTaskStartToCloseTimeout: StrictStr | None = None
    defaultTaskHeartbeatTimeout: StrictStr | None = None
    defaultTaskList: SWFTaskList | None = None
    defaultTaskPriority: StrictStr | None = None
    defaultTaskScheduleToStartTimeout: StrictStr | None = None
    defaultTaskScheduleToCloseTimeout: StrictStr | None = None
