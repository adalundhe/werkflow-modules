from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFWorkflowExecutionFailedEventAttributes(BaseModel):
    reason: StrictStr | None = None
    details: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
