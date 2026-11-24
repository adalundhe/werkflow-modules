from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SWFWorkflowExecutionCanceledEventAttributes(BaseModel):
    details: StrictStr | None = None
    decisionTaskCompletedEventId: StrictInt | None = None
