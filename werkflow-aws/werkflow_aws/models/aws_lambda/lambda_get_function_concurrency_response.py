from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class LambdaGetFunctionConcurrencyResponse(BaseModel):
    ReservedConcurrentExecutions: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
