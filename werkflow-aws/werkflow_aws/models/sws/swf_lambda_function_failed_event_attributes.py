from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFLambdaFunctionFailedEventAttributes(BaseModel):
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
    reason: StrictStr | None = None
    details: StrictStr | None = None
