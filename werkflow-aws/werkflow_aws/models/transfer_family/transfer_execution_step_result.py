from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_execution_error import TransferExecutionError


class TransferExecutionStepResult(BaseModel):
    StepType: StrictStr | None = None
    Outputs: StrictStr | None = None
    Error: TransferExecutionError | None = None
