from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_error_object import LambdaErrorObject


class LambdaSendDurableExecutionCallbackFailureRequest(BaseModel):
    CallbackId: StrictStr
    Error: LambdaErrorObject | None = None
