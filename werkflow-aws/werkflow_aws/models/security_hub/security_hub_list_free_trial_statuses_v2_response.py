from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_account_free_trial_status import SecurityHubAccountFreeTrialStatus


class SecurityHubListFreeTrialStatusesV2Response(BaseModel):
    AccountFreeTrialStatuses: list[SecurityHubAccountFreeTrialStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
