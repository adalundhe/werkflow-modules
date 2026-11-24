from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaEventPauseReason(BaseModel):
    Payload: StrictStr | None = None
    Truncated: StrictBool | None = None
