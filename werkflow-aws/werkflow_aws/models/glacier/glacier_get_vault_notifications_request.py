from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierGetVaultNotificationsRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
