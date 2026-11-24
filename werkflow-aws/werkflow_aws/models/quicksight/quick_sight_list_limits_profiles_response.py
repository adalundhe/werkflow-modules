from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_limits_profile import QuickSightLimitsProfile


class QuickSightListLimitsProfilesResponse(BaseModel):
    profiles: list[QuickSightLimitsProfile] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
