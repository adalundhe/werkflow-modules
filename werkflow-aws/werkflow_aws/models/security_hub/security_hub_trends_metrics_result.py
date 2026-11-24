from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_trends_values import SecurityHubTrendsValues


class SecurityHubTrendsMetricsResult(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    TrendsValues: SecurityHubTrendsValues | None = None
