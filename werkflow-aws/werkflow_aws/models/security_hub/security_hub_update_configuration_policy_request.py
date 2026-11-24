from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_policy import SecurityHubPolicy


class SecurityHubUpdateConfigurationPolicyRequest(BaseModel):
    Identifier: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    UpdatedReason: StrictStr | None = None
    ConfigurationPolicy: SecurityHubPolicy | None = None
