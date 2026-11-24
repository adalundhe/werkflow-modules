from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_findings_trends_filters import SecurityHubFindingsTrendsFilters


class SecurityHubGetFindingsTrendsV2Request(BaseModel):
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    Filters: SecurityHubFindingsTrendsFilters | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
