from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferWorkflowDetail(BaseModel):
    WorkflowId: StrictStr | None = None
    ExecutionRole: StrictStr | None = None
