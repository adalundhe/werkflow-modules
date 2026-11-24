from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFScheduleLambdaFunctionFailedEventAttributes(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    cause: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
