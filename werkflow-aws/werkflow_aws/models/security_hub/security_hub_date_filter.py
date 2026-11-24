from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_date_range import SecurityHubDateRange


class SecurityHubDateFilter(BaseModel):
    Start: StrictStr | None = None
    End: StrictStr | None = None
    DateRange: SecurityHubDateRange | None = None
