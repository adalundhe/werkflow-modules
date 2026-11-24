from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_profile_limit_value import QuickSightProfileLimitValue


class QuickSightLimitsProfile(BaseModel):
    profileId: StrictStr | None = None
    arn: StrictStr | None = None
    accountId: StrictStr | None = None
    profileName: StrictStr | None = None
    description: StrictStr | None = None
    resourceLimits: dict[StrictStr, QuickSightProfileLimitValue] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
