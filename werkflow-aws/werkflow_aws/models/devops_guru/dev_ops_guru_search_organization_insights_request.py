from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_search_organization_insights_filters import DevOpsGuruSearchOrganizationInsightsFilters
from .dev_ops_guru_start_time_range import DevOpsGuruStartTimeRange


class DevOpsGuruSearchOrganizationInsightsRequest(BaseModel):
    AccountIds: list[StrictStr]
    StartTimeRange: DevOpsGuruStartTimeRange
    Type: Literal['REACTIVE', 'PROACTIVE']
    Filters: DevOpsGuruSearchOrganizationInsightsFilters | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
