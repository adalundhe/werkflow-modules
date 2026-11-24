from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMSendAutomationSignalRequest(BaseModel):
    AutomationExecutionId: StrictStr
    SignalType: Literal['Approve', 'Reject', 'StartStep', 'StopStep', 'Resume', 'Revoke']
    Payload: dict[StrictStr, list[StrictStr]] | None = None
