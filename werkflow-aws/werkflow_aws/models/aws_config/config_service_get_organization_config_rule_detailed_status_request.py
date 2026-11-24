from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .config_service_status_detail_filters import ConfigServiceStatusDetailFilters


class ConfigServiceGetOrganizationConfigRuleDetailedStatusRequest(BaseModel):
    OrganizationConfigRuleName: StrictStr
    Filters: ConfigServiceStatusDetailFilters | None = None
    Limit: StrictInt | None = None
    NextToken: StrictStr | None = None
