from __future__ import annotations
from pydantic import BaseModel
from .lambda_on_failure import LambdaOnFailure
from .lambda_on_success import LambdaOnSuccess


class LambdaDestinationConfig(BaseModel):
    OnSuccess: LambdaOnSuccess | None = None
    OnFailure: LambdaOnFailure | None = None
