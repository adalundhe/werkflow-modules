from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_operation_update import LambdaOperationUpdate


class LambdaCheckpointDurableExecutionRequest(BaseModel):
    DurableExecutionArn: StrictStr
    CheckpointToken: StrictStr
    Updates: list[LambdaOperationUpdate] | None = None
    ClientToken: StrictStr | None = None
