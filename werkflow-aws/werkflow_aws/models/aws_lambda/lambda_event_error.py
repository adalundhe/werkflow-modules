from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lambda_error_object import LambdaErrorObject


class LambdaEventError(BaseModel):
    Payload: LambdaErrorObject | None = None
    Truncated: StrictBool | None = None
