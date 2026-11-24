from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_activity_window import GuardDutyActivityWindow


class GuardDutyFindingDetail(BaseModel):
    FindingId: StrictStr | None = None
    FindingType: StrictStr | None = None
    Severity: StrictStr | None = None
    AccountId: StrictStr | None = None
    Region: StrictStr | None = None
    ActivityWindow: GuardDutyActivityWindow | None = None
