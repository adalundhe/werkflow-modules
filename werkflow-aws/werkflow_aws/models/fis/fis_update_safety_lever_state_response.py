from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_safety_lever import FISSafetyLever


class FISUpdateSafetyLeverStateResponse(BaseModel):
    safetyLever: FISSafetyLever | None = None
    ResponseMetadata: dict[str, Any] | None = None
