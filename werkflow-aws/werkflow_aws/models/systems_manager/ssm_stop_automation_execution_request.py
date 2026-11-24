from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMStopAutomationExecutionRequest(BaseModel):
    AutomationExecutionId: StrictStr
    Type: Literal['Complete', 'Cancel'] | None = None
