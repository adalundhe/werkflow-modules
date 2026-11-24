from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFWorkflowExecutionFilter(BaseModel):
    workflowId: StrictStr
