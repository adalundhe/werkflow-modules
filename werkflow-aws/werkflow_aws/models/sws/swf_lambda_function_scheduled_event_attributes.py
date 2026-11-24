from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFLambdaFunctionScheduledEventAttributes(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    control: StrictStr | None = None
    input: StrictStr | None = None
    startToCloseTimeout: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
