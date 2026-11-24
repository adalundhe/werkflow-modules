from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFLambdaFunctionCompletedEventAttributes(BaseModel):
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
    result: StrictStr | None = None
