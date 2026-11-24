from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .lambda_event_input import LambdaEventInput


class LambdaExecutionStartedDetails(BaseModel):
    Input: LambdaEventInput | None = None
    ExecutionTimeout: StrictInt | None = None
