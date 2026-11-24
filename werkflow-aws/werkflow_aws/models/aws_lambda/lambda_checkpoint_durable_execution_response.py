from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_checkpoint_updated_execution_state import LambdaCheckpointUpdatedExecutionState


class LambdaCheckpointDurableExecutionResponse(BaseModel):
    CheckpointToken: StrictStr | None = None
    NewExecutionState: LambdaCheckpointUpdatedExecutionState | None = None
    ResponseMetadata: dict[str, Any] | None = None
