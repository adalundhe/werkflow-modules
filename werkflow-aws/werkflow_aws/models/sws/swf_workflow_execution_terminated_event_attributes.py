from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFWorkflowExecutionTerminatedEventAttributes(BaseModel):
    reason: StrictStr | None = None
    details: StrictStr | None = None
    childPolicy: StrictStr | None = None
    cause: StrictStr | None = None
