from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFStartLambdaFunctionFailedEventAttributes(BaseModel):
    scheduledEventId: StrictInt | None = None
    cause: StrictStr | None = None
    message: StrictStr | None = None
