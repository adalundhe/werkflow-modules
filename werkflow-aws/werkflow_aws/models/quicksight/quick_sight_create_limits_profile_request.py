from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_profile_limit_value import QuickSightProfileLimitValue


class QuickSightCreateLimitsProfileRequest(BaseModel):
    accountId: StrictStr
    profileName: StrictStr
    resourceLimits: dict[Literal['INDEX_STORAGE', 'AGENT_HOURS'], QuickSightProfileLimitValue]
    clientToken: StrictStr
    description: StrictStr | None = None
