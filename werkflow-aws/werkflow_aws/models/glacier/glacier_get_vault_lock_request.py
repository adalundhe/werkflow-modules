from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierGetVaultLockRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
