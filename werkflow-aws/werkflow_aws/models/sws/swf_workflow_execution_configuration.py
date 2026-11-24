from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFWorkflowExecutionConfiguration(BaseModel):
    taskStartToCloseTimeout: StrictStr | None = None
    executionStartToCloseTimeout: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    childPolicy: StrictStr | None = None
    lambdaRole: StrictStr | None = None
