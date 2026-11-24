from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_result import LambdaEventResult
from .lambda_retry_details import LambdaRetryDetails


class LambdaStepSucceededDetails(BaseModel):
    Result: LambdaEventResult | None = None
    RetryDetails: LambdaRetryDetails | None = None
