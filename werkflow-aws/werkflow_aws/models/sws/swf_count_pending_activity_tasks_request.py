from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFCountPendingActivityTasksRequest(BaseModel):
    domain: StrictStr
    taskList: SWFTaskList
