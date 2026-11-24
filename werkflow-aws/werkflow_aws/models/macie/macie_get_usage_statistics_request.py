from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_usage_statistics_filter import MacieUsageStatisticsFilter
from .macie_usage_statistics_sort_by import MacieUsageStatisticsSortBy


class MacieGetUsageStatisticsRequest(BaseModel):
    filterBy: list[MacieUsageStatisticsFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    sortBy: MacieUsageStatisticsSortBy | None = None
    timeRange: Literal['MONTH_TO_DATE', 'PAST_30_DAYS'] | None = None
