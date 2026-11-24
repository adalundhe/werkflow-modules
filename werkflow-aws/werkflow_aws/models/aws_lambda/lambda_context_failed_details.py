from __future__ import annotations
from pydantic import BaseModel
from .lambda_event_error import LambdaEventError


class LambdaContextFailedDetails(BaseModel):
    Error: LambdaEventError | None = None
