from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_vault_access_policy import GlacierVaultAccessPolicy


class GlacierSetVaultAccessPolicyRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    policy: GlacierVaultAccessPolicy | None = None
