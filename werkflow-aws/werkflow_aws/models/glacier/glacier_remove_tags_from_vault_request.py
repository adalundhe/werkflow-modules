from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierRemoveTagsFromVaultRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    TagKeys: list[StrictStr] | None = None
