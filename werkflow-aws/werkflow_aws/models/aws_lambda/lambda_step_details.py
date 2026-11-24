from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lambda_error_object import LambdaErrorObject


class LambdaStepDetails(BaseModel):
    Attempt: StrictInt | None = None
    NextAttemptTimestamp: datetime.datetime | StrictStr | None = None
    Result: StrictStr | None = None
    Error: LambdaErrorObject | None = None
