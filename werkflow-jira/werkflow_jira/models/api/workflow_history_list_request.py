from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowHistoryListRequest(BaseModel):
    workflowId: StrictStr | None = None
