from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_error import LambdaEventError
from .lambda_retry_details import LambdaRetryDetails


class LambdaStepFailedDetails(BaseModel):
    Error: LambdaEventError | None = None
    RetryDetails: LambdaRetryDetails | None = None
