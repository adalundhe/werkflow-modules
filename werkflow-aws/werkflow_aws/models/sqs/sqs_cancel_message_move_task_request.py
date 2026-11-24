from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SQSCancelMessageMoveTaskRequest(BaseModel):
    TaskHandle: StrictStr
