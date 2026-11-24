from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transfer_listed_execution import TransferListedExecution


class TransferListExecutionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    WorkflowId: StrictStr | None = None
    Executions: list[TransferListedExecution] | None = None
    ResponseMetadata: dict[str, Any] | None = None
