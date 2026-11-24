from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class WorkflowHistoryReadRequest(BaseModel):
    version: StrictInt | None = None
    workflowId: StrictStr | None = None
