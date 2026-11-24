from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_resources_trends_values import SecurityHubResourcesTrendsValues


class SecurityHubResourcesTrendsMetricsResult(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    TrendsValues: SecurityHubResourcesTrendsValues | None = None
