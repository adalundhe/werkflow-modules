from __future__ import annotations
from pydantic import BaseModel
from .security_hub_target import SecurityHubTarget


class SecurityHubGetConfigurationPolicyAssociationRequest(BaseModel):
    Target: SecurityHubTarget
