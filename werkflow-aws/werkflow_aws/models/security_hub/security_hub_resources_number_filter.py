from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_number_filter import SecurityHubNumberFilter


class SecurityHubResourcesNumberFilter(BaseModel):
    FieldName: StrictStr | None = None
    Filter: SecurityHubNumberFilter | None = None
