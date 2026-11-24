from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_string_filter import SecurityHubStringFilter


class SecurityHubResourcesStringFilter(BaseModel):
    FieldName: StrictStr | None = None
    Filter: SecurityHubStringFilter | None = None
