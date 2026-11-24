from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFSignalExternalWorkflowExecutionDecisionAttributes(BaseModel):
    workflowId: StrictStr
    signalName: StrictStr
    runId: StrictStr | None = None
    input: StrictStr | None = None
    control: StrictStr | None = None
