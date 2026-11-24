from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_environment_error import LambdaEnvironmentError


class LambdaEnvironmentResponse(BaseModel):
    Variables: dict[StrictStr, StrictStr] | None = None
    Error: LambdaEnvironmentError | None = None
