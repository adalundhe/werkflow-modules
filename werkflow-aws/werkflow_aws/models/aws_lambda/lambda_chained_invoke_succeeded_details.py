from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_result import LambdaEventResult


class LambdaChainedInvokeSucceededDetails(BaseModel):
    Result: LambdaEventResult | None = None
