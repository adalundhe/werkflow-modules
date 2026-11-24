from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTGetCommandExecutionRequest(BaseModel):
    executionId: StrictStr
    targetArn: StrictStr
    includeResult: StrictBool | None = None
