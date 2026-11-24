from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFRequestCancelExternalWorkflowExecutionDecisionAttributes(BaseModel):
    workflowId: StrictStr
    runId: StrictStr | None = None
    control: StrictStr | None = None
