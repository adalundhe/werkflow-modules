from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_search_insights_filters import DevOpsGuruSearchInsightsFilters
from .dev_ops_guru_start_time_range import DevOpsGuruStartTimeRange


class DevOpsGuruSearchInsightsRequest(BaseModel):
    StartTimeRange: DevOpsGuruStartTimeRange
    Type: Literal['REACTIVE', 'PROACTIVE']
    Filters: DevOpsGuruSearchInsightsFilters | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
