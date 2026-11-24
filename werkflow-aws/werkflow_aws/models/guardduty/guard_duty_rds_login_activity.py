from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_activity_window import GuardDutyActivityWindow
from .guard_duty_enrichment import GuardDutyEnrichment


class GuardDutyRdsLoginActivity(BaseModel):
    Outcome: StrictStr | None = None
    Rate: StrictStr | None = None
    AnomalyContext: StrictStr | None = None
    LoginCount: StrictInt | None = None
    ActivityWindow: GuardDutyActivityWindow | None = None
    Enrichment: GuardDutyEnrichment | None = None
