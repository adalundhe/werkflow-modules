from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_map_filter import SecurityHubMapFilter


class SecurityHubResourcesMapFilter(BaseModel):
    FieldName: StrictStr | None = None
    Filter: SecurityHubMapFilter | None = None
