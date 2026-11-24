from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeLimitsProfileRequest(BaseModel):
    profileId: StrictStr
    accountId: StrictStr
