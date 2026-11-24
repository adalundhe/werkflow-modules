from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRequestCancelWorkflowExecutionRequest(BaseModel):
    domain: StrictStr
    workflowId: StrictStr
    runId: StrictStr | None = None
