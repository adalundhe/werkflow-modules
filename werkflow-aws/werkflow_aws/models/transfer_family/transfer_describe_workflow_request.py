from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeWorkflowRequest(BaseModel):
    WorkflowId: StrictStr
