from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_workflow_execution import SWFWorkflowExecution


class SWFWorkflowExecutionSignaledEventAttributes(BaseModel):
    signalName: StrictStr | None = None
    input: StrictStr | None = None
    externalWorkflowExecution: SWFWorkflowExecution | None = None
    externalInitiatedEventId: StrictInt | None = None
