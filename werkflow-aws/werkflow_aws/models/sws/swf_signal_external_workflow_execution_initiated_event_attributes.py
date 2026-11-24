from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFSignalExternalWorkflowExecutionInitiatedEventAttributes(BaseModel):
    workflowId: StrictStr | None = None
    runId: StrictStr | None = None
    signalName: StrictStr | None = None
    input: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
    control: StrictStr | None = None
