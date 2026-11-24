from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_list_anomalies_for_insight_filters import DevOpsGuruListAnomaliesForInsightFilters
from .dev_ops_guru_start_time_range import DevOpsGuruStartTimeRange


class DevOpsGuruListAnomaliesForInsightRequest(BaseModel):
    InsightId: StrictStr
    StartTimeRange: DevOpsGuruStartTimeRange | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    AccountId: StrictStr | None = None
    Filters: DevOpsGuruListAnomaliesForInsightFilters | None = None
