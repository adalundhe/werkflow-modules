from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFSignalExternalWorkflowExecutionFailedEventAttributes(BaseModel):
    workflowId: StrictStr | None = None
    runId: StrictStr | None = None
    cause: StrictStr | None = None
    initiatedEventId: StrictInt | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    control: StrictStr | None = None
