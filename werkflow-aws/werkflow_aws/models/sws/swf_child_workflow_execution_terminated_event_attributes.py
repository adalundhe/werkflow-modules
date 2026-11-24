from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .swf_workflow_execution import SWFWorkflowExecution
from .swf_workflow_type import SWFWorkflowType


class SWFChildWorkflowExecutionTerminatedEventAttributes(BaseModel):
    workflowExecution: SWFWorkflowExecution | None = None
    workflowType: SWFWorkflowType | None = None
    initiatedEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
