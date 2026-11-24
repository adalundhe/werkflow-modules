from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_member_account_ranking import GuardDutyMemberAccountRanking


class GuardDutyAccountOverview(BaseModel):
    AccountId: StrictStr | None = None
    AccountStatus: StrictStr | None = None
    DetectorId: StrictStr | None = None
    Region: StrictStr | None = None
    DelegatedAdminAccountId: StrictStr | None = None
    TotalMemberAccounts: StrictInt | None = None
    TotalFindings: StrictInt | None = None
    AffectedAccountCount: StrictInt | None = None
    AccountRankings: list[GuardDutyMemberAccountRanking] | None = None
