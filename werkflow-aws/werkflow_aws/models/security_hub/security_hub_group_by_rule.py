from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_ocsf_finding_filters import SecurityHubOcsfFindingFilters


class SecurityHubGroupByRule(BaseModel):
    GroupByField: StrictStr
    Filters: SecurityHubOcsfFindingFilters | None = None
