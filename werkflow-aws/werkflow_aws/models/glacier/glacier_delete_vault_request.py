from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierDeleteVaultRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
