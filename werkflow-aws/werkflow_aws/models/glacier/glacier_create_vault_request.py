from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierCreateVaultRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
