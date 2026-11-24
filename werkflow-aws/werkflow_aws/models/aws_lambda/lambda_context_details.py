from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lambda_error_object import LambdaErrorObject


class LambdaContextDetails(BaseModel):
    ReplayChildren: StrictBool | None = None
    Result: StrictStr | None = None
    Error: LambdaErrorObject | None = None
