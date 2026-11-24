from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_task_list import SWFTaskList
from .swf_workflow_type import SWFWorkflowType


class SWFWorkflowExecutionContinuedAsNewEventAttributes(BaseModel):
    input: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    newExecutionRunId: StrictStr | None = None
    executionStartToCloseTimeout: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    taskStartToCloseTimeout: StrictStr | None = None
    childPolicy: StrictStr | None = None
    tagList: list[StrictStr] | None = None
    workflowType: SWFWorkflowType | None = None
    lambdaRole: StrictStr | None = None
