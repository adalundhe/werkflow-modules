from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class WAFv2CheckCapacityResponse(BaseModel):
    Capacity: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
