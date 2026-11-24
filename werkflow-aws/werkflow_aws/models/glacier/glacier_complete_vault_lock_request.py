from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierCompleteVaultLockRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    lockId: StrictStr
