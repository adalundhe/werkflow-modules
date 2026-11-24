from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierListTagsForVaultRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
