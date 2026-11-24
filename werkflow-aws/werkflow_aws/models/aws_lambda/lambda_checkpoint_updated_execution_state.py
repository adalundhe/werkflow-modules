from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_operation import LambdaOperation


class LambdaCheckpointUpdatedExecutionState(BaseModel):
    Operations: list[LambdaOperation] | None = None
    NextMarker: StrictStr | None = None
