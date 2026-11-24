from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_string_filter import SecurityHubStringFilter


class SecurityHubFindingsTrendsStringFilter(BaseModel):
    FieldName: Literal['account_id', 'region', 'finding_types', 'finding_status', 'finding_cve_ids', 'finding_compliance_status', 'finding_control_id', 'finding_class_name', 'finding_provider', 'finding_activity_name', 'resource_cloud_providers', 'resource_regions', 'resource_owner_ids', 'resource_owner_organization_ids'] | None = None
    Filter: SecurityHubStringFilter | None = None
