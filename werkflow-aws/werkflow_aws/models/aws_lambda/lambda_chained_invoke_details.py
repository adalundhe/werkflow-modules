from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_error_object import LambdaErrorObject


class LambdaChainedInvokeDetails(BaseModel):
    Result: StrictStr | None = None
    Error: LambdaErrorObject | None = None
