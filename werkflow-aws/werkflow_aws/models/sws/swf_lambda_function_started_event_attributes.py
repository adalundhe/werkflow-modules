from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SWFLambdaFunctionStartedEventAttributes(BaseModel):
    scheduledEventId: StrictInt | None = None
