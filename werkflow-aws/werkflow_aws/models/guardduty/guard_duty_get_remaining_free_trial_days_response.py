from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .guard_duty_account_free_trial_info import GuardDutyAccountFreeTrialInfo
from .guard_duty_unprocessed_account import GuardDutyUnprocessedAccount


class GuardDutyGetRemainingFreeTrialDaysResponse(BaseModel):
    Accounts: list[GuardDutyAccountFreeTrialInfo] | None = None
    UnprocessedAccounts: list[GuardDutyUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
