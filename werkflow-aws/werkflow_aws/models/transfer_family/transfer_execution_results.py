from __future__ import annotations
from pydantic import BaseModel
from .transfer_execution_step_result import TransferExecutionStepResult


class TransferExecutionResults(BaseModel):
    Steps: list[TransferExecutionStepResult] | None = None
    OnExceptionSteps: list[TransferExecutionStepResult] | None = None
