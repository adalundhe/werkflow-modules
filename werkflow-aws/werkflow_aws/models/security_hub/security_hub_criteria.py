from __future__ import annotations
from pydantic import BaseModel
from .security_hub_ocsf_finding_filters import SecurityHubOcsfFindingFilters
from .security_hub_resources_filters import SecurityHubResourcesFilters


class SecurityHubCriteria(BaseModel):
    OcsfFindingCriteria: SecurityHubOcsfFindingFilters | None = None
    ResourceCriteria: SecurityHubResourcesFilters | None = None
