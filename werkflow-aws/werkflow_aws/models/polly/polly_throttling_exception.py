from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .polly_throttling_reason import PollyThrottlingReason


class PollyThrottlingException(BaseModel):
    message: StrictStr | None = None
    throttlingReasons: list[PollyThrottlingReason] | None = None
