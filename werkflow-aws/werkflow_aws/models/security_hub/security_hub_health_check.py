from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_health_issue import SecurityHubHealthIssue


class SecurityHubHealthCheck(BaseModel):
    ConnectorStatus: StrictStr | None = None
    Message: StrictStr | None = None
    LastCheckedAt: datetime.datetime | StrictStr | None = None
    Issues: list[SecurityHubHealthIssue] | None = None
