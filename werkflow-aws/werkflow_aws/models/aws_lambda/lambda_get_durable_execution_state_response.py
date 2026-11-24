from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_operation import LambdaOperation


class LambdaGetDurableExecutionStateResponse(BaseModel):
    Operations: list[LambdaOperation] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
