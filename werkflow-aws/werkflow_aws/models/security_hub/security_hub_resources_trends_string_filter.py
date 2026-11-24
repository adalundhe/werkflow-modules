from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_string_filter import SecurityHubStringFilter


class SecurityHubResourcesTrendsStringFilter(BaseModel):
    FieldName: Literal['account_id', 'region', 'resource_type', 'resource_category', 'resource_cloud_provider', 'resource_region', 'resource_owner_id', 'resource_owner_organization_id'] | None = None
    Filter: SecurityHubStringFilter | None = None
