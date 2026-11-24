from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaSendDurableExecutionCallbackHeartbeatRequest(BaseModel):
    CallbackId: StrictStr
