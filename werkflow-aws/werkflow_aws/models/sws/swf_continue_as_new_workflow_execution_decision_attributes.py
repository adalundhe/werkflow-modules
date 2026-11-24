from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFContinueAsNewWorkflowExecutionDecisionAttributes(BaseModel):
    input: StrictStr | None = None
    executionStartToCloseTimeout: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    taskStartToCloseTimeout: StrictStr | None = None
    childPolicy: Literal['TERMINATE', 'REQUEST_CANCEL', 'ABANDON'] | None = None
    tagList: list[StrictStr] | None = None
    workflowTypeVersion: StrictStr | None = None
    lambdaRole: StrictStr | None = None
