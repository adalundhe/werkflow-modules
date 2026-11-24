from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_policy import SecurityHubPolicy


class SecurityHubCreateConfigurationPolicyRequest(BaseModel):
    Name: StrictStr
    ConfigurationPolicy: SecurityHubPolicy
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
