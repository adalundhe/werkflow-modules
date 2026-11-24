from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierAddTagsToVaultRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
