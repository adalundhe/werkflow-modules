from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_string_filter import SecurityHubStringFilter


class SecurityHubSoftwareStringFilter(BaseModel):
    FieldName: Literal['AccountId', 'PackageName', 'PackageVersion', 'PackageType', 'Region', 'ResourceRegion', 'ResourceType', 'ResourceId', 'ResourceProvider', 'ResourceOwnerAccountId', 'ResourceOwnerOrgId', 'ResourceCloudPartition'] | None = None
    Filter: SecurityHubStringFilter | None = None
