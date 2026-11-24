from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transfer_described_workflow import TransferDescribedWorkflow


class TransferDescribeWorkflowResponse(BaseModel):
    Workflow: TransferDescribedWorkflow | None = None
    ResponseMetadata: dict[str, Any] | None = None
