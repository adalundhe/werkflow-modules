from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList
from .swf_workflow_type import SWFWorkflowType


class SWFStartWorkflowExecutionRequest(BaseModel):
    domain: StrictStr
    workflowId: StrictStr
    workflowType: SWFWorkflowType
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    input: StrictStr | None = None
    executionStartToCloseTimeout: StrictStr | None = None
    tagList: list[StrictStr] | None = None
    taskStartToCloseTimeout: StrictStr | None = None
    childPolicy: Literal['TERMINATE', 'REQUEST_CANCEL', 'ABANDON'] | None = None
    lambdaRole: StrictStr | None = None
