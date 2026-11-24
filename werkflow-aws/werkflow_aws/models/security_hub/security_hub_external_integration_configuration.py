from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubExternalIntegrationConfiguration(BaseModel):
    ConnectorArn: StrictStr | None = None
