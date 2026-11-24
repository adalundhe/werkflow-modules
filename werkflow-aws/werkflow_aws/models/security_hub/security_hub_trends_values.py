from __future__ import annotations
from pydantic import BaseModel
from .security_hub_severity_trends_count import SecurityHubSeverityTrendsCount


class SecurityHubTrendsValues(BaseModel):
    SeverityTrends: SecurityHubSeverityTrendsCount | None = None
