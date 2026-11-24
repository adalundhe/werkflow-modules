from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFFailWorkflowExecutionDecisionAttributes(BaseModel):
    reason: StrictStr | None = None
    details: StrictStr | None = None
