from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_free_trial_status import SecurityHubFreeTrialStatus


class SecurityHubAccountFreeTrialStatus(BaseModel):
    AccountId: StrictStr | None = None
    EvaluatedAt: datetime.datetime | StrictStr | None = None
    FreeTrialStatuses: list[SecurityHubFreeTrialStatus] | None = None
