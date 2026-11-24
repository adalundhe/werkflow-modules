from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteLimitsProfileRequest(BaseModel):
    profileId: StrictStr
    accountId: StrictStr
