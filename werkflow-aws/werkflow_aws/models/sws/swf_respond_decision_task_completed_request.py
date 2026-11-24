from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_decision import SWFDecision
from .swf_task_list import SWFTaskList


class SWFRespondDecisionTaskCompletedRequest(BaseModel):
    taskToken: StrictStr
    decisions: list[SWFDecision] | None = None
    executionContext: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskListScheduleToStartTimeout: StrictStr | None = None
