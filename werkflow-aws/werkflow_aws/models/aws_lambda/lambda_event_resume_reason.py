from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LambdaEventResumeReason(BaseModel):
    Payload: StrictStr | None = None
    Truncated: StrictBool | None = None
