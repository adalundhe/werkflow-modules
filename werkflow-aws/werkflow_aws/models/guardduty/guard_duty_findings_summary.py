from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .guard_duty_finding_type_count import GuardDutyFindingTypeCount
from .guard_duty_severity_breakdown import GuardDutySeverityBreakdown
from .guard_duty_time_window_group import GuardDutyTimeWindowGroup


class GuardDutyFindingsSummary(BaseModel):
    TotalFindings: StrictInt | None = None
    SeverityBreakdown: GuardDutySeverityBreakdown | None = None
    TopFindingTypes: list[GuardDutyFindingTypeCount] | None = None
    ByTimeWindow: list[GuardDutyTimeWindowGroup] | None = None
