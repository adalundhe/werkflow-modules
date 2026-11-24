from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteCommandExecutionRequest(BaseModel):
    executionId: StrictStr
    targetArn: StrictStr
