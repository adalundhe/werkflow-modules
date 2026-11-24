from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_security_finding_filters import SecurityHubAwsSecurityFindingFilters


class SecurityHubInsight(BaseModel):
    InsightArn: StrictStr | None = None
    Name: StrictStr | None = None
    Filters: SecurityHubAwsSecurityFindingFilters | None = None
    GroupByAttribute: StrictStr | None = None
