from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_filter_criterion import GuardDutyFilterCriterion


class GuardDutyFilterCriteria(BaseModel):
    FilterCriterion: list[GuardDutyFilterCriterion] | None = None
