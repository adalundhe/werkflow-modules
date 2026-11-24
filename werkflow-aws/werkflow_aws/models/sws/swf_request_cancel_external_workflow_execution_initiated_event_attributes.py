from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFRequestCancelExternalWorkflowExecutionInitiatedEventAttributes(BaseModel):
    workflowId: StrictStr | None = None
    runId: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    control: StrictStr | None = None
