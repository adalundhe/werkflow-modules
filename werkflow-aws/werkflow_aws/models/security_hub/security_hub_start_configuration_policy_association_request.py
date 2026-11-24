from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_target import SecurityHubTarget


class SecurityHubStartConfigurationPolicyAssociationRequest(BaseModel):
    ConfigurationPolicyIdentifier: StrictStr
    Target: SecurityHubTarget
