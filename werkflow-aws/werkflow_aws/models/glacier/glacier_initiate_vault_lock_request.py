from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_vault_lock_policy import GlacierVaultLockPolicy


class GlacierInitiateVaultLockRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    policy: GlacierVaultLockPolicy | None = None
