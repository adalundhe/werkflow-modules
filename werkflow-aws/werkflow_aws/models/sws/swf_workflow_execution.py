from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFWorkflowExecution(BaseModel):
    workflowId: StrictStr | None = None
    runId: StrictStr | None = None
