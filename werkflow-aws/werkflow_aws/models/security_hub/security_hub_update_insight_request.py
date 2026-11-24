from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_security_finding_filters import SecurityHubAwsSecurityFindingFilters


class SecurityHubUpdateInsightRequest(BaseModel):
    InsightArn: StrictStr
    Name: StrictStr | None = None
    Filters: SecurityHubAwsSecurityFindingFilters | None = None
    GroupByAttribute: StrictStr | None = None
