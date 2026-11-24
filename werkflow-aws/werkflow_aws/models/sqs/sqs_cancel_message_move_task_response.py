from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class SQSCancelMessageMoveTaskResponse(BaseModel):
    ApproximateNumberOfMessagesMoved: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
