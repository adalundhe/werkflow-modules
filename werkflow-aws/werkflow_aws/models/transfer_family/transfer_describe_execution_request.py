from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferDescribeExecutionRequest(BaseModel):
    ExecutionId: StrictStr
    WorkflowId: StrictStr
