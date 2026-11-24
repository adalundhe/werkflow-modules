from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFWorkflowExecutionCompletedEventAttributes(BaseModel):
    result: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
