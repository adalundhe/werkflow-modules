from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_event import LambdaEvent


class LambdaGetDurableExecutionHistoryResponse(BaseModel):
    Events: list[LambdaEvent] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
