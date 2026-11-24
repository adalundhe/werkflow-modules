from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowCopyRequest(BaseModel):
    description: StrictStr | None = None
    workflowId: StrictStr | None = None
    workflowName: StrictStr | None = None
