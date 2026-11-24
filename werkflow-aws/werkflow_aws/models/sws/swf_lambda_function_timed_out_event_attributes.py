from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFLambdaFunctionTimedOutEventAttributes(BaseModel):
    scheduledEventId: StrictInt | None = None
    startedEventId: StrictInt | None = None
    timeoutType: StrictStr | None = None
