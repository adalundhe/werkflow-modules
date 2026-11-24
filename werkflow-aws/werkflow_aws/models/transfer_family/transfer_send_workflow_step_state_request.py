from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TransferSendWorkflowStepStateRequest(BaseModel):
    WorkflowId: StrictStr
    ExecutionId: StrictStr
    Token: StrictStr
    Status: Literal['SUCCESS', 'FAILURE']
