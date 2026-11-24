from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_workflow_type import SWFWorkflowType


class SWFStartChildWorkflowExecutionFailedEventAttributes(BaseModel):
    workflowType: SWFWorkflowType | None = None
    cause: StrictStr | None = None
    workflowId: StrictStr | None = None
    initiatedEventId: StrictInt | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    control: StrictStr | None = None
