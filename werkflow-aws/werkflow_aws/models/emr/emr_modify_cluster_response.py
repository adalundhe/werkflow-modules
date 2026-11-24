from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt


class EMRModifyClusterResponse(BaseModel):
    StepConcurrencyLevel: StrictInt | None = None
    ExtendedSupport: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
