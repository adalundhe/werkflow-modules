from __future__ import annotations
from pydantic import BaseModel
from .security_hub_resource_owner_account import SecurityHubResourceOwnerAccount
from .security_hub_resource_owner_org import SecurityHubResourceOwnerOrg


class SecurityHubResourceOwner(BaseModel):
    Account: SecurityHubResourceOwnerAccount | None = None
    Org: SecurityHubResourceOwnerOrg | None = None
