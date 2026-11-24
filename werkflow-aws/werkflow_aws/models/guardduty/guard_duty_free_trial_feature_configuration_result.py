from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyFreeTrialFeatureConfigurationResult(BaseModel):
    Name: StrictStr | None = None
    FreeTrialDaysRemaining: StrictInt | None = None
