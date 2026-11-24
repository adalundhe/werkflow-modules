from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFWorkflowExecutionTimedOutEventAttributes(BaseModel):
    timeoutType: StrictStr | None = None
    childPolicy: StrictStr | None = None
