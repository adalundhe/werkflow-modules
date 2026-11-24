from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsSendTaskHeartbeatRequest(BaseModel):
    taskToken: StrictStr
