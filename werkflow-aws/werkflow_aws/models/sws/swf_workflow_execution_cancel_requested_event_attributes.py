from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_workflow_execution import SWFWorkflowExecution


class SWFWorkflowExecutionCancelRequestedEventAttributes(BaseModel):
    externalWorkflowExecution: SWFWorkflowExecution | None = None
    externalInitiatedEventId: StrictInt | None = None
    cause: StrictStr | None = None
