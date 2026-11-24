from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchPartialFailure(BaseModel):
    FailureResource: StrictStr | None = None
    ExceptionType: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureDescription: StrictStr | None = None
