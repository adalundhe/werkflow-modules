from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_boolean_filter import SecurityHubBooleanFilter


class SecurityHubOcsfBooleanFilter(BaseModel):
    FieldName: StrictStr | None = None
    Filter: SecurityHubBooleanFilter | None = None
