from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_cspm_health_check import SecurityHubCspmHealthCheck
from .security_hub_cspm_provider_detail import SecurityHubCspmProviderDetail


class SecurityHubGetConnectorResponse(BaseModel):
    ConnectorArn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    Health: SecurityHubCspmHealthCheck | None = None
    ProviderDetail: SecurityHubCspmProviderDetail | None = None
    CreatedBy: StrictStr | None = None
    EnablementStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
