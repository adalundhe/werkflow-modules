from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_error_object import LambdaErrorObject


class LambdaStopDurableExecutionRequest(BaseModel):
    DurableExecutionArn: StrictStr
    Error: LambdaErrorObject | None = None
