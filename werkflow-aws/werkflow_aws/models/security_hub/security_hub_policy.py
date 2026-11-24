from __future__ import annotations
from pydantic import BaseModel
from .security_hub_policy_model import SecurityHubPolicyModel


class SecurityHubPolicy(BaseModel):
    SecurityHub: SecurityHubPolicyModel | None = None
