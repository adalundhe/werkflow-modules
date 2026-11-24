from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationSummary(BaseModel):
    InvestigationId: StrictStr | None = None
    Status: StrictStr | None = None
    TriggerPrompt: StrictStr | None = None
    RiskLevel: StrictStr | None = None
    Confidence: StrictStr | None = None
    Title: StrictStr | None = None
    InvestigationType: StrictStr | None = None
    FindingId: StrictStr | None = None
    AccountId: StrictStr | None = None
    AdminAccountId: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
