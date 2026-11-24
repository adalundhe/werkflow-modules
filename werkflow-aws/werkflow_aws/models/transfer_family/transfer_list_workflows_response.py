from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_workflow import TransferListedWorkflow


class TransferListWorkflowsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Workflows: list[TransferListedWorkflow] | None = None
    ResponseMetadata: dict[str, Any] | None = None
