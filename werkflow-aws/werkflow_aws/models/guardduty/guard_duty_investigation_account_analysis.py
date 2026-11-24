from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_baseline import GuardDutyBaseline
from .guard_duty_trend import GuardDutyTrend


class GuardDutyInvestigationAccountAnalysis(BaseModel):
    Trend: GuardDutyTrend | None = None
    Baseline: GuardDutyBaseline | None = None
