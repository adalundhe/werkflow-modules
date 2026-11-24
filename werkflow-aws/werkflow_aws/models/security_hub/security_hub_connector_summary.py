from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_provider_summary import SecurityHubProviderSummary


class SecurityHubConnectorSummary(BaseModel):
    ConnectorArn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ProviderSummary: SecurityHubProviderSummary | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    EnablementStatus: StrictStr | None = None
    EnablementStatusReason: StrictStr | None = None
