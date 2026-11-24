from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFCompleteWorkflowExecutionDecisionAttributes(BaseModel):
    result: StrictStr | None = None
