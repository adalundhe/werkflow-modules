from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_protection_plan import GuardDutyProtectionPlan


class GuardDutyDetectionCoverage(BaseModel):
    ProtectionPlans: list[GuardDutyProtectionPlan] | None = None
    FoundationalDataSources: list[StrictStr] | None = None
    CoverageGaps: StrictStr | None = None
    KeyObservation: StrictStr | None = None
