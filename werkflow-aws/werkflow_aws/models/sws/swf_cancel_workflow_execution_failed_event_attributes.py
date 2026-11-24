from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFCancelWorkflowExecutionFailedEventAttributes(BaseModel):
    cause: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
