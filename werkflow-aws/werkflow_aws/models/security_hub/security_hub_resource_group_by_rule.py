from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_resources_filters import SecurityHubResourcesFilters


class SecurityHubResourceGroupByRule(BaseModel):
    GroupByField: Literal['AccountId', 'AccountName', 'Region', 'ResourceProvider', 'ResourceOwnerAccountId', 'ResourceOwnerOrgId', 'ResourceCloudPartition', 'ResourceRegion', 'ResourceCategory', 'ResourceType', 'ResourceName', 'FindingsSummary.FindingType', 'ResourceSubCategory', 'DiscoveryType', 'ResourceInfo.AIDetails.HostResourceType', 'ResourceInfo.AIDetails.CanonicalId', 'ResourceCriticality']
    Filters: SecurityHubResourcesFilters | None = None
