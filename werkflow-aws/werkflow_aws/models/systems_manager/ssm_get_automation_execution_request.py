from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetAutomationExecutionRequest(BaseModel):
    AutomationExecutionId: StrictStr
