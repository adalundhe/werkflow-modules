from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDeleteWorkflowRequest(BaseModel):
    WorkflowId: StrictStr
