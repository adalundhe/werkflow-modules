from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_ocsf_finding_filters import SecurityHubOcsfFindingFilters


class SecurityHubFindingsOutput(BaseModel):
    Format: StrictStr | None = None
    Filters: SecurityHubOcsfFindingFilters | None = None
    SelectedFields: list[StrictStr] | None = None
