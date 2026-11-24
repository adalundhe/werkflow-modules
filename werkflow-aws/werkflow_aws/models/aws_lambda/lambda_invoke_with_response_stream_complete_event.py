from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaInvokeWithResponseStreamCompleteEvent(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorDetails: StrictStr | None = None
    LogResult: StrictStr | None = None
