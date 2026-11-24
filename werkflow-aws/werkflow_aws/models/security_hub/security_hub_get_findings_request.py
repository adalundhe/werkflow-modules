from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_security_finding_filters import SecurityHubAwsSecurityFindingFilters
from .security_hub_sort_criterion import SecurityHubSortCriterion


class SecurityHubGetFindingsRequest(BaseModel):
    Filters: SecurityHubAwsSecurityFindingFilters | None = None
    SortCriteria: list[SecurityHubSortCriterion] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
