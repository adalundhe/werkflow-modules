from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_profile_limit_value import QuickSightProfileLimitValue


class QuickSightUpdateLimitsProfileRequest(BaseModel):
    profileId: StrictStr
    accountId: StrictStr
    profileName: StrictStr | None = None
    description: StrictStr | None = None
    resourceLimits: dict[Literal['INDEX_STORAGE', 'AGENT_HOURS'], QuickSightProfileLimitValue] | None = None
