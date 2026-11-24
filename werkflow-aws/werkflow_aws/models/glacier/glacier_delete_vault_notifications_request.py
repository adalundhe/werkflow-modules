from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierDeleteVaultNotificationsRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
