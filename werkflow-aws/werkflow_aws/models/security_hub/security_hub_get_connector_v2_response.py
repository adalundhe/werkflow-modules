from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_health_check import SecurityHubHealthCheck
from .security_hub_provider_detail import SecurityHubProviderDetail


class SecurityHubGetConnectorV2Response(BaseModel):
    ConnectorArn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    Health: SecurityHubHealthCheck | None = None
    ProviderDetail: SecurityHubProviderDetail | None = None
    EnablementStatus: StrictStr | None = None
    EnablementStatusReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
