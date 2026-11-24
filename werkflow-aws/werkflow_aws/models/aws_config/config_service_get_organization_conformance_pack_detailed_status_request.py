from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_organization_resource_detailed_status_filters import ConfigServiceOrganizationResourceDetailedStatusFilters


class ConfigServiceGetOrganizationConformancePackDetailedStatusRequest(BaseModel):
    OrganizationConformancePackName: StrictStr
    Filters: ConfigServiceOrganizationResourceDetailedStatusFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
