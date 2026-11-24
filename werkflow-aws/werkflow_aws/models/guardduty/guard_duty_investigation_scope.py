from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_query_time_window import GuardDutyQueryTimeWindow


class GuardDutyInvestigationScope(BaseModel):
    InvestigationType: StrictStr | None = None
    FindingId: StrictStr | None = None
    AccountId: StrictStr | None = None
    AdminAccountId: StrictStr | None = None
    QueryTimeWindow: GuardDutyQueryTimeWindow | None = None
