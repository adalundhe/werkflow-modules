from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_effective_limit import QuickSightEffectiveLimit


class QuickSightUserLimits(BaseModel):
    userName: StrictStr | None = None
    namespace: StrictStr | None = None
    effectiveLimits: list[QuickSightEffectiveLimit] | None = None
