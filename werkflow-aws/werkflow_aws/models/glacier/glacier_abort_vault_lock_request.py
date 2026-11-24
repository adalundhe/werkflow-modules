from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierAbortVaultLockRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
