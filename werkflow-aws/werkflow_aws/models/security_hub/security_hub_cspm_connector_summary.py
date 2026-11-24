from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_cspm_provider_summary import SecurityHubCspmProviderSummary


class SecurityHubCspmConnectorSummary(BaseModel):
    ConnectorArn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ProviderSummary: SecurityHubCspmProviderSummary | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    EnablementStatus: StrictStr | None = None
