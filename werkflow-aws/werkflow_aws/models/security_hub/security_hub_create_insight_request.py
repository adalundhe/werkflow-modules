from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_security_finding_filters import SecurityHubAwsSecurityFindingFilters


class SecurityHubCreateInsightRequest(BaseModel):
    Name: StrictStr
    Filters: SecurityHubAwsSecurityFindingFilters
    GroupByAttribute: StrictStr
