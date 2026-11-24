from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFCancelWorkflowExecutionDecisionAttributes(BaseModel):
    details: StrictStr | None = None
