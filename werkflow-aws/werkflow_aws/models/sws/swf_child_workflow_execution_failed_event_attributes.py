from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_workflow_execution import SWFWorkflowExecution
from .swf_workflow_type import SWFWorkflowType


class SWFChildWorkflowExecutionFailedEventAttributes(BaseModel):
    workflowExecution: SWFWorkflowExecution | None = None
    workflowType: SWFWorkflowType | None = None
    reason: StrictStr | None = None
    details: StrictStr | None = None
    initiatedEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
