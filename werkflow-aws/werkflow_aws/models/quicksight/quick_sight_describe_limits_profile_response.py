from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .quick_sight_limits_profile import QuickSightLimitsProfile


class QuickSightDescribeLimitsProfileResponse(BaseModel):
    profile: QuickSightLimitsProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
