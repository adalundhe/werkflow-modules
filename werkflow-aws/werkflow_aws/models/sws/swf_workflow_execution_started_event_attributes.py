from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_task_list import SWFTaskList
from .swf_workflow_execution import SWFWorkflowExecution
from .swf_workflow_type import SWFWorkflowType


class SWFWorkflowExecutionStartedEventAttributes(BaseModel):
    input: StrictStr | None = None
    executionStartToCloseTimeout: StrictStr | None = None
    taskStartToCloseTimeout: StrictStr | None = None
    childPolicy: StrictStr | None = None
    taskList: SWFTaskList | None = None
    taskPriority: StrictStr | None = None
    workflowType: SWFWorkflowType | None = None
    tagList: list[StrictStr] | None = None
    continuedExecutionRunId: StrictStr | None = None
    parentWorkflowExecution: SWFWorkflowExecution | None = None
    parentInitiatedEventId: StrictInt | None = None
    lambdaRole: StrictStr | None = None
