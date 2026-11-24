from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .swf_workflow_execution import SWFWorkflowExecution


class SWFExternalWorkflowExecutionSignaledEventAttributes(BaseModel):
    workflowExecution: SWFWorkflowExecution | None = None
    initiatedEventId: StrictInt | None = None
