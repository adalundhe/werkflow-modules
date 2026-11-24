from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_account_statistics import GuardDutyAccountStatistics
from .guard_duty_date_statistics import GuardDutyDateStatistics
from .guard_duty_finding_type_statistics import GuardDutyFindingTypeStatistics
from .guard_duty_resource_statistics import GuardDutyResourceStatistics
from .guard_duty_severity_statistics import GuardDutySeverityStatistics


class GuardDutyFindingStatistics(BaseModel):
    CountBySeverity: dict[StrictStr, StrictInt] | None = None
    GroupedByAccount: list[GuardDutyAccountStatistics] | None = None
    GroupedByDate: list[GuardDutyDateStatistics] | None = None
    GroupedByFindingType: list[GuardDutyFindingTypeStatistics] | None = None
    GroupedByResource: list[GuardDutyResourceStatistics] | None = None
    GroupedBySeverity: list[GuardDutySeverityStatistics] | None = None
