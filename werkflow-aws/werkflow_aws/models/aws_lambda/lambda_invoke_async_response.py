from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class LambdaInvokeAsyncResponse(BaseModel):
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
