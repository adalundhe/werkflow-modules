from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_software_filters import SecurityHubSoftwareFilters


class SecurityHubSoftwareGroupByRule(BaseModel):
    GroupByField: Literal['AccountId', 'PackageName', 'PackageVersion', 'PackageType', 'Region', 'ResourceRegion', 'ResourceType', 'ResourceId', 'ResourceProvider', 'ResourceOwnerAccountId', 'ResourceOwnerOrgId', 'ResourceCloudPartition']
    Filters: SecurityHubSoftwareFilters | None = None
