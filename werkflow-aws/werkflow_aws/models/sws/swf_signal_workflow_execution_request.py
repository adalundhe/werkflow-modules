from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFSignalWorkflowExecutionRequest(BaseModel):
    domain: StrictStr
    workflowId: StrictStr
    signalName: StrictStr
    runId: StrictStr | None = None
    input: StrictStr | None = None
