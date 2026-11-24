from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_resources_trends_filters import SecurityHubResourcesTrendsFilters


class SecurityHubGetResourcesTrendsV2Request(BaseModel):
    StartTime: datetime.datetime | StrictStr
    EndTime: datetime.datetime | StrictStr
    Filters: SecurityHubResourcesTrendsFilters | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
