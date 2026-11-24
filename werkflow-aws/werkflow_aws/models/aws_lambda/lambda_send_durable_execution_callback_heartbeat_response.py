from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class LambdaSendDurableExecutionCallbackHeartbeatResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
