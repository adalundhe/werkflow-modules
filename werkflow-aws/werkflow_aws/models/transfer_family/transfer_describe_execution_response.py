from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_described_execution import TransferDescribedExecution


class TransferDescribeExecutionResponse(BaseModel):
    WorkflowId: StrictStr | None = None
    Execution: TransferDescribedExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None
