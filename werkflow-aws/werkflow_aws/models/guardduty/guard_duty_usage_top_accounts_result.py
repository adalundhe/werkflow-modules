from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_usage_top_account_result import GuardDutyUsageTopAccountResult


class GuardDutyUsageTopAccountsResult(BaseModel):
    Feature: StrictStr | None = None
    Accounts: list[GuardDutyUsageTopAccountResult] | None = None
