from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_date_filter import SecurityHubDateFilter


class SecurityHubResourcesDateFilter(BaseModel):
    FieldName: StrictStr | None = None
    Filter: SecurityHubDateFilter | None = None
