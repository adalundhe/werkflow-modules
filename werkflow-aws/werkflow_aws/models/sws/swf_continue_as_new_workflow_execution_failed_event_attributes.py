from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFContinueAsNewWorkflowExecutionFailedEventAttributes(BaseModel):
    cause: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
