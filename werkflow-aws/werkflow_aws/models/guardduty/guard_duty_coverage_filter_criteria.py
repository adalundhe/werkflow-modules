from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_coverage_filter_criterion import GuardDutyCoverageFilterCriterion


class GuardDutyCoverageFilterCriteria(BaseModel):
    FilterCriterion: list[GuardDutyCoverageFilterCriterion] | None = None
