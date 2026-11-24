from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_result import LambdaEventResult


class LambdaExecutionSucceededDetails(BaseModel):
    Result: LambdaEventResult | None = None
