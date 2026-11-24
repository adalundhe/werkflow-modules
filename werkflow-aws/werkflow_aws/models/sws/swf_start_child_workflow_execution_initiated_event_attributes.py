from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_task_list import SWFTaskList
from .swf_workflow_type import SWFWorkflowType


class SWFStartChildWorkflowExecutionInitiatedEventAttributes(BaseModel):
    workflowId: StrictStr | None = None
    workflowType: SWFWorkflowType | None = None
    control: StrictStr | None = None
    input: StrictStr | None = None
    executionStartToCloseTimeout: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    childPolicy: StrictStr | None = None
    taskStartToCloseTimeout: StrictStr | None = None
    tagList: list[StrictStr] | None = None
    lambdaRole: StrictStr | None = None
