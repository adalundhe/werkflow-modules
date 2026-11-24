from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .guard_duty_usage_criteria import GuardDutyUsageCriteria


class GuardDutyGetUsageStatisticsRequest(BaseModel):
    DetectorId: StrictStr
    UsageStatisticType: Literal['SUM_BY_ACCOUNT', 'SUM_BY_DATA_SOURCE', 'SUM_BY_RESOURCE', 'TOP_RESOURCES', 'SUM_BY_FEATURES', 'TOP_ACCOUNTS_BY_FEATURE']
    UsageCriteria: GuardDutyUsageCriteria
    Unit: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
