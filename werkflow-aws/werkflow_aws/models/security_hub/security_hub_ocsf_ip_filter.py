from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_ip_filter import SecurityHubIpFilter


class SecurityHubOcsfIpFilter(BaseModel):
    FieldName: StrictStr | None = None
    Filter: SecurityHubIpFilter | None = None
