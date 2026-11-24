from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFPollForActivityTaskRequest(BaseModel):
    domain: StrictStr
    taskList: SWFTaskList
    identity: StrictStr | None = None
